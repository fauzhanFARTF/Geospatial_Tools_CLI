import geopandas as gpd
import sys
from pathlib import Path

def check_projection(file_path):
    try:
        # Membaca file geospasial
        gdf = gpd.read_file(file_path)
        
        # Mendapatkan sistem koordinat
        crs = gdf.crs
        
        if crs:
            print(f"File: {file_path}")
            print(f"Sistem Koordinat (CRS): {crs}")
        else:
            print(f"File: {file_path}")
            print("Sistem Koordinat tidak ditemukan atau tidak terdefinisi.")
    except Exception as e:
        print(f"Error membaca file {file_path}: {e}")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_base_folder = BASE_DIR / "data/input"

    # Pastikan folder ada
    if not input_base_folder.exists():
        print(f"Folder {input_base_folder} tidak ditemukan.")
        sys.exit(1)
    
    # Loop semua file dalam folder dan subfolder
    for file in input_base_folder.rglob("*"):
        if file.is_file() and file.suffix.lower() in [".shp", ".geojson", ".kml", ".gdb"]:  # Filter format geospasial
            check_projection(file)
        else:
            print(f"File {file} dilewati (bukan format geospasial).")
