import os
import geopandas as gpd
import fiona
from datetime import datetime

# Definisikan direktori dasar proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Direktori input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_geojson_to_kml(input_folder, output_folder):
    """
    Mengonversi semua file GeoJSON dalam folder input dan subfoldernya ke format KML,
    mempertahankan struktur direktori dan menambahkan timestamp pada nama file output
    untuk file yang berada langsung di dalam folder input.

    :param input_folder: Path ke folder yang berisi file GeoJSON
    :param output_folder: Path ke folder untuk menyimpan file KML
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Aktifkan driver KML untuk fiona
    fiona.supported_drivers['KML'] = 'rw'

    # Telusuri folder input dan subfoldernya
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.geojson'):
                geojson_file = os.path.join(root, file)
                try:
                    # Get the file name without extension
                    filename = os.path.splitext(file)[0]
                    
                    # Get the current timestamp
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    
                    # Determine the relative path of the KML file with respect to the input folder
                    relative_path = os.path.relpath(root, input_folder)
                    
                    # Construct the output directory path
                    if relative_path == '.':
                        # If the KML file is directly in the input folder
                        folder_output = output_folder
                    else:
                        # If the KML file is in a subfolder
                        folder_output = os.path.join(output_folder, relative_path)
                    
                    os.makedirs(folder_output, exist_ok=True)
                    
                    # Path for the output GeoJSON file with timestamp
                    output_kml = os.path.join(folder_output, f"{filename}_{timestamp}.kml")

                    # Baca file GeoJSON dan konversi ke KML
                    gdf = gpd.read_file(geojson_file)
                    gdf.to_file(output_kml, driver='KML')

                    print(f"✅ {geojson_file} berhasil dikonversi ke {output_kml}")

                except Exception as e:
                    print(f"❌ Gagal mengonversi {geojson_file}: {e}")
            else:
                print(f"⚠️ Melewati file {file} karena bukan file GeoJSON.")
                
if __name__ == "__main__":
    print(f"📂 Folder Input: {input_folder}")
    print(f"📂 Folder Output: {output_folder}\n")

    convert_geojson_to_kml(input_folder, output_folder)
