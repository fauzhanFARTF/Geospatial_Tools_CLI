import geopandas as gpd
import os
import glob

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_kml_to_geojson(input_folder, output_folder):
    """
    Mengonversi semua file KML dalam folder input ke format GeoJSON.
    File GeoJSON langsung disimpan di folder output tanpa subfolder tambahan.

    :param input_folder: Path folder yang berisi file KML
    :param output_folder: Path folder untuk menyimpan file GeoJSON
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Cari semua file .kml dalam folder input
    kml_files = glob.glob(os.path.join(input_folder, "*.kml"))

    if not kml_files:
        print(f"❌ Tidak ada file KML di folder input: {input_folder}")
        return

    for kml_path in kml_files:
        try:
            # Ambil nama file KML tanpa ekstensi
            kml_name = os.path.splitext(os.path.basename(kml_path))[0]

            print(f"🔄 Mengonversi {kml_name}.kml ke GeoJSON...")

            # Path output untuk GeoJSON (langsung dalam folder output)
            output_geojson = os.path.join(output_folder, f"{kml_name}.geojson")

            # Baca KML dan simpan sebagai GeoJSON
            gdf = gpd.read_file(kml_path)
            gdf.to_file(output_geojson, driver="GeoJSON")

            print(f"✅ {kml_name}.kml berhasil dikonversi ke {output_geojson}")

        except Exception as e:
            print(f"❌ Gagal mengonversi {kml_path}: {e}")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_kml_to_geojson(input_folder, output_folder)
