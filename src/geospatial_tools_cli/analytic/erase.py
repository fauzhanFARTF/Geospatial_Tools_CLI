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
    geospatial_files = [file for file in folder_path.rglob("*") if file.suffix.lower() in supported_formats]

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

    for subdir in input_base_folder.iterdir():
        if subdir.is_dir():
            print(f"🔍 Memproses direktori: {subdir.name}")

            input_files = find_geospatial_files(subdir)
            output_subdir = output_base_folder / f"{subdir.name}_{timestamp}_erase"
            output_subdir.mkdir(parents=True, exist_ok=True)

            for input_file in input_files:
                input_extension = input_file.suffix.lower()
                output_folder = output_subdir

                for coverage_file in coverage_files:
                    print(f"🔄 Menghapus area {input_file.name} dari {coverage_file.name}")

                    if input_file.suffix.lower() == ".kml" or coverage_file.suffix.lower() == ".kml":
                        fiona.drvsupport.supported_drivers["KML"] = "rw"

                    try:
                        gdf_input = gpd.read_file(input_file)
                        gdf_coverage = gpd.read_file(coverage_file)

                        print(f"📌 {input_file.name} - Geometry Type: {gdf_input.geom_type.unique()}")
                        print(f"📌 {coverage_file.name} - Geometry Type: {gdf_coverage.geom_type.unique()}")

                        result = gpd.overlay(gdf_input, gdf_coverage, how='difference', keep_geom_type=False)

                        output_driver = {
                            ".shp": "ESRI Shapefile",
                            ".kml": "KML",
                            ".geojson": "GeoJSON"
                        }.get(input_extension, None)

                        if output_driver is None:
                            print(f"❌ Format {input_extension} tidak didukung!")
                            continue

                        output_file = output_folder / f"{input_file.stem}{input_extension}"
                        result.to_file(output_file, driver=output_driver)
                        print(f"✅ Hasil erase disimpan di: {output_file}")

                    except Exception as e:
                        print(f"⚠️ Gagal mengolah {input_file.name}: {e}")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_base_folder = BASE_DIR / "data/input"
    input_coverage_folder = BASE_DIR / "data/input_coverage"
    output_base_folder = BASE_DIR / "data/output"
    
    geospatial_erase(input_base_folder, input_coverage_folder, output_base_folder)
