import geopandas as gpd
import os
from datetime import datetime
import shutil

# Tentukan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_geojson_to_shp_and_zip(input_folder, output_folder):
    """
    Mengonversi semua file GeoJSON dalam folder input dan subfoldernya ke format Shapefile (SHP),
    menyimpannya dalam folder output dengan struktur yang mirip dengan folder input,
    menambahkan timestamp pada nama folder output, dan mengarsipkannya ke dalam file ZIP.

    :param input_folder: Path folder yang berisi file GeoJSON
    :param output_folder: Path folder untuk menyimpan file SHP dan arsip ZIP
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Traversal rekursif melalui folder input
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.geojson'):
                geojson_file = os.path.join(root, file)
                try:
                    # Ambil nama file tanpa ekstensi
                    filename = os.path.splitext(file)[0]
                    
                    # Dapatkan timestamp saat ini
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    
                    # Tentukan path relatif dari file GeoJSON terhadap folder input
                    relative_path = os.path.relpath(root, input_folder)
                    
                    if relative_path == '.':
                        # Jika file GeoJSON berada langsung di dalam folder input
                        folder_output = os.path.join(output_folder, f"{filename}_{timestamp}")
                    else:
                        # Jika file GeoJSON berada di dalam subfolder
                        folder_output = os.path.join(output_folder, relative_path, f"{filename}_{timestamp}")
                    
                    os.makedirs(folder_output, exist_ok=True)
                    
                    # Path untuk output SHP
                    output_shp = os.path.join(folder_output, f"{filename}.shp")
                    
                    # Baca GeoJSON dan konversi ke SHP
                    gdf = gpd.read_file(geojson_file)
                    gdf.to_file(output_shp, driver='ESRI Shapefile')
                    
                    print(f"✅ {geojson_file} berhasil dikonversi ke {output_shp}")

                except Exception as e:
                    print(f"❌ Gagal mengonversi {geojson_file}: {e}")
            else:
                print(f"⚠️ Melewati file {file} karena bukan file GeoJSON.")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_geojson_to_shp_and_zip(input_folder, output_folder)
