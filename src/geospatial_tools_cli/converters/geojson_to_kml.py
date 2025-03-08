import os
import geopandas as gpd
from pathlib import Path
from datetime import datetime

def convert_geojson_to_kml(source_directory, destination_directory):
    """Mengonversi semua file GeoJSON menjadi KML dengan struktur yang diinginkan."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination_directory = Path(destination_directory)
    destination_directory.mkdir(parents=True, exist_ok=True)
    
    for file_path in Path(source_directory).rglob("*.geojson"):
        relative_path = file_path.relative_to(source_directory)
        parts = list(relative_path.parts)
        
        # Tambahkan timestamp ke setiap bagian folder
        new_parts = [f"{part}_{timestamp}_kml" for part in parts[:-1]]
        new_parts.append(parts[-1].replace(".geojson", f"_{timestamp}.kml"))
        
        output_path = destination_directory / Path(*new_parts)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            gdf = gpd.read_file(file_path)
            gdf.to_file(output_path, driver='KML')
            print(f"✅ Converted: {file_path} -> {output_path}")
        except Exception as e:
            print(f"❌ Error converting {file_path}: {e}")

def main():
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_folder = BASE_DIR / "data/input"
    output_folder = BASE_DIR / "data/output"
    
    if not input_folder.exists():
        print(f"⚠️ Folder {input_folder} tidak ditemukan.")
        exit(1)
    
    print(f"📂 Processing GeoJSON files from: {input_folder}\n")
    convert_geojson_to_kml(input_folder, output_folder)

if __name__ == "__main__":
    main()
