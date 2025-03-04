import geopandas as gpd
import os
import glob

# Tentukan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_shp_to_geojson(input_folder, output_folder):
    """
    Mengonversi semua file SHP dalam subfolder ke GeoJSON, tanpa mempertahankan struktur folder input.
    File GeoJSON disimpan langsung di folder output.

    :param input_folder: Path folder utama yang berisi file SHP dalam subfolder
    :param output_folder: Path folder utama untuk menyimpan file GeoJSON
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Cari semua file .shp dalam folder input dan subfoldernya
    shp_files = glob.glob(os.path.join(input_folder, "**", "*.shp"), recursive=True)

    if not shp_files:
        print(f"❌ Tidak ada file SHP di folder input: {input_folder}")
        return

    for shp_path in shp_files:
        try:
            # Ambil nama file SHP tanpa ekstensi
            shp_name = os.path.splitext(os.path.basename(shp_path))[0]

            # Path output untuk GeoJSON (langsung di folder output)
            output_geojson = os.path.join(output_folder, f"{shp_name}.geojson")

            print(f"🔄 Mengonversi {shp_name}.shp ke GeoJSON...")

            # Baca SHP dan simpan sebagai GeoJSON
            gdf = gpd.read_file(shp_path)
            gdf.to_file(output_geojson, driver="GeoJSON")

            print(f"✅ {shp_name}.shp berhasil dikonversi ke {output_geojson}")

        except Exception as e:
            print(f"❌ Gagal mengonversi {shp_path}: {e}")

if __name__ == "__main__":
    print(f"📂 Folder Input: {input_folder}")
    print(f"📂 Folder Output: {output_folder}\n")

    convert_shp_to_geojson(input_folder, output_folder)
