import os
import datetime
from pathlib import Path
import geopandas as gpd
import fiona

def find_geospatial_files(folder_path):
    """Mencari file geospasial (GeoJSON, KML, SHP) di dalam folder utama."""
    folder_path = Path(folder_path)

    if not folder_path.exists():
        raise FileNotFoundError(f"❌ Folder {folder_path} tidak ditemukan!")

    supported_formats = {".geojson", ".kml", ".shp"}
    geospatial_files = [
        file for file in folder_path.glob("*")  # Hanya ambil file di folder utama
        if file.suffix.lower() in supported_formats
    ]

    print(f"🔍 Menemukan {len(geospatial_files)} file di {folder_path}:")
    for file in geospatial_files:
        print(f"  - {file}")  # ✅ Debugging: Pastikan file ditemukan

    if not geospatial_files:
        raise FileNotFoundError(f"⚠️ Tidak ada file geospasial ditemukan di {folder_path}.")

    return geospatial_files

def geospatial_erase(input_base_folder, input_coverage_folder, output_base_folder):
    """Melakukan operasi erase antara file geospasial di folder input dan file coverage."""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    input_base_folder = Path(input_base_folder)
    input_coverage_folder = Path(input_coverage_folder)
    output_base_folder = Path(output_base_folder)

    if not input_coverage_folder.exists():
        raise FileNotFoundError(f"❌ Folder coverage {input_coverage_folder} tidak ditemukan!")

    coverage_files = find_geospatial_files(input_coverage_folder)

    # Proses file yang langsung ada di `input/`
    input_files = find_geospatial_files(input_base_folder)

    print("✅ Memulai proses erase...")

    for input_file in input_files:
        input_extension = input_file.suffix.lower()
        output_folder = output_base_folder
        output_folder.mkdir(parents=True, exist_ok=True)

        for coverage_file in coverage_files:
            print(f"\n🔄 Processing erase: {input_file.name} ⨉ {coverage_file.name}...")

            # Pastikan driver KML dapat dibaca
            if input_file.suffix.lower() == ".kml" or coverage_file.suffix.lower() == ".kml":
                fiona.drvsupport.supported_drivers["KML"] = "rw"

            try:
                gdf_input = gpd.read_file(input_file)
                gdf_coverage = gpd.read_file(coverage_file)

                # Menampilkan jumlah fitur sebelum proses erase
                print(f"📌 {input_file.name} memiliki {len(gdf_input)} feature.")
                print(f"📌 {coverage_file.name} memiliki {len(gdf_coverage)} feature.")

                if gdf_input.empty or gdf_coverage.empty:
                    print(f"⚠️ Salah satu dataset kosong, melewati file ini...")
                    continue  # Skip file yang kosong

                # Melakukan operasi ERASE
                print("🚀 Melakukan operasi ERASE...")
                result = gpd.overlay(gdf_input, gdf_coverage, how='difference', keep_geom_type=False)

                if result.empty:
                    print(f"⚠️ Hasil erase kosong untuk {input_file.name}!")
                    continue

                print(f"✅ Hasil erase memiliki {len(result)} feature.")

                # Tentukan format output berdasarkan format input
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
                    raise ValueError(f"❌ Format {input_extension} tidak didukung!")

                output_file = output_folder / f"{input_file.stem}_erase{output_extension}"
                result.to_file(output_file, driver=output_driver)
                print(f"✅ Hasil erase disimpan di: {output_file}")

            except Exception as e:
                print(f"❌ ERROR: Gagal mengolah {input_file.name}: {e}")

    print("\n🎉 Proses erase selesai!")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_base_folder = BASE_DIR / "data/input"
    input_coverage_folder = BASE_DIR / "data/input_coverage"
    output_base_folder = BASE_DIR / "data/output"
    
    geospatial_erase(input_base_folder, input_coverage_folder, output_base_folder)
