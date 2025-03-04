import geopandas as gpd
import os
import glob

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_geojson_to_kml(input_folder, output_folder):
    """
    Mengonversi semua file GeoJSON dalam folder input ke format KML,
    dan menyimpan hasilnya langsung di folder output.

    :param input_folder: Path folder yang berisi file GeoJSON
    :param output_folder: Path folder untuk menyimpan file KML
    """
    os.makedirs(output_folder, exist_ok=True)  # Buat folder output jika belum ada

    # Cari semua file GeoJSON dalam folder input
    geojson_files = glob.glob(os.path.join(input_folder, "*.geojson"))

    if not geojson_files:
        print(f"❌ Tidak ada file GeoJSON di folder input: {input_folder}")
        return

    for geojson_file in geojson_files:
        try:
            # Ambil nama file tanpa ekstensi
            filename = os.path.splitext(os.path.basename(geojson_file))[0]

            # Path untuk output KML (langsung ke folder output tanpa sub-folder)
            output_kml = os.path.join(output_folder, f"{filename}.kml")
            
            # Baca GeoJSON
            gdf = gpd.read_file(geojson_file)
            
            # Simpan sebagai KML dalam folder output
            gdf.to_file(output_kml, driver="KML")

            print(f"✅ {geojson_file} berhasil dikonversi ke {output_kml}")
        
        except Exception as e:
            print(f"❌ Gagal mengonversi {geojson_file}: {e}")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_geojson_to_kml(input_folder, output_folder)
