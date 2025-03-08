import os
import shutil
import geopandas as gpd
from pathlib import Path
from datetime import datetime

def convert_kml_to_shp(source_directory, destination_directory):
    """Mengonversi semua file KML menjadi Shapefile dengan struktur yang diinginkan."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination_directory = Path(destination_directory)
    destination_directory.mkdir(parents=True, exist_ok=True)
    
    for file_path in Path(source_directory).rglob("*.kml"):
        relative_path = file_path.relative_to(source_directory)
        parts = list(relative_path.parts)
        
        # Tambahkan timestamp ke setiap bagian folder
        new_parts = [f"{part}_{timestamp}_shp" for part in parts[:-1]]
        new_parts.append(parts[-1].replace(".kml", f"_{timestamp}"))
        
        new_folder = destination_directory / Path(*new_parts)
        new_folder.mkdir(parents=True, exist_ok=True)
        
        shp_path = new_folder / (file_path.stem + ".shp")
        
        try:
            gdf = gpd.read_file(file_path)
            gdf.to_file(shp_path, driver='ESRI Shapefile')
            print(f"✅ Converted: {file_path} -> {shp_path}")
        except Exception as e:
            print(f"❌ Error converting {file_path}: {e}")

def main():
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_folder = BASE_DIR / "data/input"
    output_folder = BASE_DIR / "data/output"
    
    if not input_folder.exists():
        print(f"⚠️ Folder {input_folder} tidak ditemukan.")
        exit(1)
    
    print(f"📂 Processing KML files from: {input_folder}\n")
    convert_kml_to_shp(input_folder, output_folder)

if __name__ == "__main__":
    main()