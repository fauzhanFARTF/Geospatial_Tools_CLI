import os
import glob
import geopandas as gpd
from datetime import datetime

def convert_shp_to_geojson(input_folder, output_folder):
    """
    Mengonversi semua file SHP dalam subfolder dan sub-subfolder ke GeoJSON,
    dengan struktur output sesuai ketentuan.

    :param input_folder: Path folder utama yang berisi file SHP dalam subfolder dan sub-subfolder
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

            # Dapatkan stempel waktu saat ini
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            # Dapatkan path relatif dari file SHP terhadap folder input
            relative_path = os.path.relpath(shp_path, input_folder)

            # Hitung jumlah level direktori
            path_levels = relative_path.split(os.sep)

            if len(path_levels) == 2:
                # Jika file berada di subfolder (input/area1/file1.shp), simpan langsung di folder output
                output_geojson = os.path.join(output_folder, f"{shp_name}_{timestamp}.geojson")
            elif len(path_levels) >= 3:
                # Jika file berada di sub-subfolder (input/region1/area1/file1.shp), simpan dalam folder sesuai nama folder input
                parent_folder = path_levels[0]
                output_subfolder = os.path.join(output_folder, parent_folder)
                os.makedirs(output_subfolder, exist_ok=True)
                output_geojson = os.path.join(output_subfolder, f"{shp_name}_{timestamp}.geojson")
            else:
                print(f"❌ Struktur folder tidak dikenali untuk file: {shp_path}")
                continue

            print(f"🔄 Mengonversi {shp_name}.shp ke GeoJSON...")

            # Baca SHP dan simpan sebagai GeoJSON
            gdf = gpd.read_file(shp_path)
            gdf.to_file(output_geojson, driver="GeoJSON")

            print(f"✅ {shp_name}.shp berhasil dikonversi ke {output_geojson}")

        except Exception as e:
            print(f"❌ Gagal mengonversi {shp_path}: {e}")

if __name__ == "__main__":
    # Tentukan path absolut dari direktori proyek
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

    # Path input dan output
    input_folder = os.path.join(BASE_DIR, "data/input")
    output_folder = os.path.join(BASE_DIR, "data/output")

    print(f"📂 Folder Input: {input_folder}")
    print(f"📂 Folder Output: {output_folder}\n")

    convert_shp_to_geojson(input_folder, output_folder)
