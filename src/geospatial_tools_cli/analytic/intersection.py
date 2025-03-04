import os
from pathlib import Path
import geopandas as gpd
import fiona

def find_geospatial_files(folder_path):
    """Mencari file geospasial (GeoJSON, KML, SHP) di folder yang ditentukan."""
    folder_path = Path(folder_path)
    
    if not folder_path.exists():
        raise FileNotFoundError(f"❌ Folder {folder_path} tidak ditemukan!")

    # Definisikan ekstensi file yang didukung dan driver yang sesuai
    supported_formats = {
        ".geojson": "GeoJSON",
        ".kml": "KML",
        ".shp": "ESRI Shapefile"
    }
    
    geospatial_files = []
    for extension, driver in supported_formats.items():
        files = list(folder_path.rglob(f"*{extension}"))
        for file in files:
            geospatial_files.append((file, driver))

    if not geospatial_files:
        print(f"⚠️ Tidak ada file geospasial yang didukung ditemukan di {folder_path}. File yang ada:")
        for file in folder_path.rglob("*.*"):
            print(f"  - {file.name}")
        raise FileNotFoundError(f"❌ Tidak ada file geospasial yang didukung di {folder_path}.")

    return geospatial_files

def geospatial_intersect(input_base_folder, input_coverage_folder, output_base_folder):
    """Melakukan intersect antara file geospasial di folder input dan file coverage."""

    # Pastikan folder input_coverage ada
    input_coverage_folder = Path(input_coverage_folder)
    if not input_coverage_folder.exists():
        raise FileNotFoundError(f"❌ Folder coverage {input_coverage_folder} tidak ditemukan!")

    # Temukan semua file coverage
    coverage_files = find_geospatial_files(input_coverage_folder)

    # Iterasi melalui setiap subdirektori di folder input base
    input_base_folder = Path(input_base_folder)
    for subdir in input_base_folder.iterdir():
        if subdir.is_dir():
            print(f"🔍 Memproses direktori: {subdir.name}")

            # Temukan file geospasial di subdirektori saat ini
            input_files = find_geospatial_files(subdir)

            # Buat subdirektori output yang sesuai
            output_subdir = Path(output_base_folder) / subdir.name
            output_subdir.mkdir(parents=True, exist_ok=True)

            # Iterasi melalui setiap file input
            for input_file, input_driver in input_files:
                # Tentukan ekstensi file input
                input_extension = input_file.suffix.lower()

                # Jika file input adalah .shp, buat subfolder berdasarkan nama file input tanpa ekstensi
                if input_extension == ".shp":
                    output_folder = output_subdir / input_file.stem
                    output_folder.mkdir(parents=True, exist_ok=True)
                else:
                    output_folder = output_subdir

                # Lakukan intersect untuk setiap file coverage
                for coverage_file, coverage_driver in coverage_files:
                    print(f"🔄 Menginterseksi {input_file.name} dengan {coverage_file.name}")

                    # Aktifkan dukungan KML jika diperlukan
                    if input_driver == "KML" or coverage_driver == "KML":
                        fiona.drvsupport.supported_drivers['LIBKML'] = 'rw'

                    # Baca file geospasial menggunakan geopandas
                    gdf_input = gpd.read_file(input_file, driver=input_driver)
                    gdf_coverage = gpd.read_file(coverage_file, driver=coverage_driver)

                    # Lakukan operasi intersect
                    result = gpd.overlay(gdf_input, gdf_coverage, how='intersection')

                    # Tentukan ekstensi dan driver file output berdasarkan driver input
                    if input_extension == ".shp":
                        output_extension = ".shp"
                        output_driver = "ESRI Shapefile"
                    elif input_extension == ".kml":
                        output_extension = ".kml"
                        output_driver = "KML"
                    elif input_extension == ".geojson":
                        output_extension = ".geojson"
                        output_driver = "GeoJSON"
                    else:
                        raise ValueError(f"❌ Ekstensi file {input_extension} tidak didukung!")

                    # Tentukan path file output
                    output_file = output_folder / f"{input_file.stem}_intersect_{coverage_file.stem}{output_extension}"

                    # Simpan hasil ke file dengan driver yang sesuai
                    result.to_file(output_file, driver=output_driver)

                    print(f"✅ Hasil intersect disimpan di: {output_file}")

if __name__ == "__main__":
    # Definisikan path folder base
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_base_folder = BASE_DIR / "data/input"
    input_coverage_folder = BASE_DIR / "data/input_coverage"
    output_base_folder = BASE_DIR / "data/output"

    # Lakukan intersect
    geospatial_intersect(input_base_folder, input_coverage_folder, output_base_folder)
0
