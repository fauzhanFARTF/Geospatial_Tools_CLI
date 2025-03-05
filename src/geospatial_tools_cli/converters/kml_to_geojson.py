import os
import geopandas as gpd
from datetime import datetime

# Definisikan direktori dasar proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Direktori input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_kml_to_geojson(input_folder, output_folder):
    """
    Mengonversi semua file KML di folder input dan subfoldernya ke format GeoJSON,
    mempertahankan struktur direktori dan menambahkan stempel waktu pada setiap file output.

    :param input_folder: Path ke folder yang berisi file KML
    :param output_folder: Path ke folder untuk menyimpan file GeoJSON
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Jelajahi folder input dan subfoldernya
    for root, _, files in os.walk(input_folder):
        for file in files:
            # Periksa apakah file memiliki ekstensi .kml (case-insensitive)
            if file.lower().endswith('.kml'):
                kml_file = os.path.join(root, file)
                try:
                    # Dapatkan nama file tanpa ekstensi
                    filename = os.path.splitext(file)[0]
                    
                    # Dapatkan stempel waktu saat ini
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    
                    # Tentukan path relatif file KML terhadap folder input
                    relative_path = os.path.relpath(root, input_folder)
                    
                    # Bangun path direktori output
                    if relative_path == '.':
                        # Jika file KML langsung berada di folder input
                        folder_output = output_folder
                    else:
                        # Jika file KML berada di subfolder
                        folder_output = os.path.join(output_folder, relative_path)
                    
                    os.makedirs(folder_output, exist_ok=True)
                    
                    # Path untuk file GeoJSON output dengan stempel waktu
                    output_geojson = os.path.join(folder_output, f"{filename}_{timestamp}.geojson")
                    
                    # Baca file KML dan konversi ke GeoJSON
                    gdf = gpd.read_file(kml_file, driver='KML')
                    gdf.to_file(output_geojson, driver='GeoJSON')
                    
                    print(f"✅ {kml_file} berhasil dikonversi ke {output_geojson}")

                except Exception as e:
                    print(f"❌ Gagal mengonversi {kml_file}: {e}")
            else:
                print(f"⚠️ Melewati file {file} karena bukan file KML.")

if __name__ == "__main__":
    print(f"📂 Folder Input: {input_folder}")
    print(f"📂 Folder Output: {output_folder}\n")

    convert_kml_to_geojson(input_folder, output_folder)
