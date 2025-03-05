import geopandas as gpd
import os
from datetime import datetime
import shutil

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_kml_to_shp_and_zip(input_folder, output_folder):
    """
    Mengonversi semua file KML dalam folder input dan subfoldernya ke format Shapefile (SHP),
    menyimpannya dalam folder output dengan struktur yang mirip dengan folder input,
    menambahkan timestamp pada nama folder output, dan mengarsipkannya ke dalam file ZIP.

    :param input_folder: Path folder yang berisi file KML
    :param output_folder: Path folder untuk menyimpan file SHP dan arsip ZIP
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
                    
                    # Buat arsip ZIP dari folder_output
                    zip_filename = f"{folder_output}.zip"
                    shutil.make_archive(folder_output, 'zip', folder_output)
                    print(f"🗜️ Folder {folder_output} berhasil diarsipkan ke {zip_filename}")

                except Exception as e:
                    print(f"❌ Gagal mengonversi {kml_file}: {e}")
            else:
                print(f"⚠️ Melewati file {file} karena bukan file KML.")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_kml_to_shp_and_zip(input_folder, output_folder)
