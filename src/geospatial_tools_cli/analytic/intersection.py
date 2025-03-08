import os
import datetime
from pathlib import Path
import geopandas as gpd
import fiona

def find_geospatial_files(folder_path):
    """Mencari file geospasial (GeoJSON, KML, SHP) di dalam folder."""
    folder_path = Path(folder_path)

    if not folder_path.exists():
        raise FileNotFoundError(f"❌ Folder {folder_path} tidak ditemukan!")

    supported_formats = {".geojson", ".kml", ".shp"}
    geospatial_files = []

    for file in folder_path.rglob("*"):
        if file.suffix.lower() in supported_formats:
            geospatial_files.append(file)

    if not geospatial_files:
        raise FileNotFoundError(f"⚠️ Tidak ada file geospasial ditemukan di {folder_path}.")

    return geospatial_files

def geospatial_intersect(input_base_folder, input_coverage_folder, output_base_folder):
    """Melakukan intersect antara file geospasial di folder input dan file coverage."""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    input_base_folder = Path(input_base_folder)
    input_coverage_folder = Path(input_coverage_folder)
    output_base_folder = Path(output_base_folder)

    if not input_coverage_folder.exists():
        raise FileNotFoundError(f"❌ Folder coverage {input_coverage_folder} tidak ditemukan!")

    coverage_files = find_geospatial_files(input_coverage_folder)

    for subdir in input_base_folder.iterdir():
        if subdir.is_dir():
            print(f"🔍 Memproses direktori: {subdir.name}")

            input_files = find_geospatial_files(subdir)
            output_subdir = output_base_folder / f"{subdir.name}_intersect_{timestamp}"
            output_subdir.mkdir(parents=True, exist_ok=True)

            for input_file in input_files:
                input_extension = input_file.suffix.lower()

                # Tangani output untuk SHP agar tidak bercampur
                if input_extension == ".shp":
                    output_folder = output_subdir / f"{input_file.stem}_intersect_{timestamp}"
                    output_folder.mkdir(parents=True, exist_ok=True)
                else:
                    output_folder = output_subdir

                for coverage_file in coverage_files:
                    print(f"🔄 Menginterseksi {input_file.name} dengan {coverage_file.name}")

                    # Pastikan driver KML dapat dibaca
                    if input_file.suffix.lower() == ".kml" or coverage_file.suffix.lower() == ".kml":
                        fiona.drvsupport.supported_drivers["KML"] = "rw"

                    try:
                        gdf_input = gpd.read_file(input_file)
                        gdf_coverage = gpd.read_file(coverage_file)

                        print(f"📌 {input_file.name} - Geometry Type: {gdf_input.geom_type.unique()}")
                        print(f"📌 {coverage_file.name} - Geometry Type: {gdf_coverage.geom_type.unique()}")

                        # Lakukan intersection
                        result = gpd.overlay(gdf_input, gdf_coverage, how='intersection', keep_geom_type=False)

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

                        output_file = output_folder / f"{input_file.stem}{output_extension}"
                        result.to_file(output_file, driver=output_driver)
                        print(f"✅ Hasil intersect disimpan di: {output_file}")

                    except Exception as e:
                        print(f"⚠️ Gagal mengolah {input_file.name}: {e}")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_base_folder = BASE_DIR / "data/input"
    input_coverage_folder = BASE_DIR / "data/input_coverage"
    output_base_folder = BASE_DIR / "data/output"
    
    geospatial_intersect(input_base_folder, input_coverage_folder, output_base_folder)
