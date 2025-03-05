import geopandas as gpd
import os
from datetime import datetime

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_kml_to_shp(input_folder, output_folder):
    """
    Mengonversi semua file KML dalam folder input dan subfoldernya ke format Shapefile (SHP),
    menyimpannya dalam folder output dengan struktur yang mirip dengan folder input,
    dan menambahkan timestamp pada nama folder output sesuai dengan aturan yang ditentukan.

    :param input_folder: Path folder yang berisi file KML
    :param output_folder: Path folder untuk menyimpan file SHP
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Traversal rekursif melalui folder input
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.kml'):
                kml_file = os.path.join(root, file)
                try:
                    # Ambil nama file tanpa ekstensi
                    filename = os.path.splitext(file)[0]
                    
                    # Dapatkan timestamp saat ini
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    
                    # Tentukan path relatif dari file KML terhadap folder input
                    relative_path = os.path.relpath(root, input_folder)
                    
                    if relative_path == '.':
                        # Jika file KML berada langsung di dalam folder input
                        folder_output = os.path.join(output_folder, f"{filename}_{timestamp}")
                    else:
                        # Jika file KML berada di dalam subfolder
                        folder_output = os.path.join(output_folder, relative_path, f"{filename}_{timestamp}")
                    
                    os.makedirs(folder_output, exist_ok=True)
                    
                    # Path untuk output SHP
                    output_shp = os.path.join(folder_output, f"{filename}.shp")
                    
                    # Baca KML dan konversi ke SHP
                    gdf = gpd.read_file(kml_file, driver='KML')
                    gdf.to_file(output_shp, driver='ESRI Shapefile')
                    
                    print(f"✅ {kml_file} berhasil dikonversi ke {output_shp}")

                except Exception as e:
                    print(f"❌ Gagal mengonversi {kml_file}: {e}")
            else:
                print(f"⚠️ Melewati file {file} karena bukan file KML.")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_kml_to_shp(input_folder, output_folder)
