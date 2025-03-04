import geopandas as gpd
import os
import glob
import zipfile
import fiona

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_gdb_to_shp_zip(input_folder, output_folder):
    """
    Mengonversi semua file GDB dalam folder input ke format Shapefile (SHP),
    menyimpan setiap layer dalam foldernya sendiri, dan mengompresnya ke ZIP.

    :param input_folder: Path folder yang berisi file GDB
    :param output_folder: Path folder untuk menyimpan file SHP dan ZIP
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Cari semua folder .gdb dalam folder input
    gdb_files = glob.glob(os.path.join(input_folder, "*.gdb"))

    if not gdb_files:
        print(f"❌ Tidak ada file GDB di folder input: {input_folder}")
        return

    for gdb_path in gdb_files:
        try:
            # Ambil nama folder GDB tanpa ekstensi
            gdb_name = os.path.splitext(os.path.basename(gdb_path))[0]
            
            # Buat folder berdasarkan nama file input
            gdb_output_folder = os.path.join(output_folder, gdb_name)
            os.makedirs(gdb_output_folder, exist_ok=True)

            # Ambil daftar layer dalam GDB
            layers = fiona.listlayers(gdb_path)

            if not layers:
                print(f"⚠️ Tidak ada layer dalam {gdb_path}, dilewati.")
                continue

            for layer in layers:
                try:
                    print(f"🔄 Mengonversi layer: {layer} dari {gdb_name}.gdb...")

                    # Buat folder khusus untuk layer ini
                    layer_folder = os.path.join(gdb_output_folder, layer)
                    os.makedirs(layer_folder, exist_ok=True)

                    # Path output untuk SHP
                    output_shp = os.path.join(layer_folder, f"{layer}.shp")

                    # Baca GDB dan simpan sebagai SHP
                    gdf = gpd.read_file(gdb_path, layer=layer)
                    gdf.to_file(output_shp, driver="ESRI Shapefile")

                except Exception as e:
                    print(f"⚠️ Gagal mengonversi layer {layer}: {e}")

            print(f"✅ {gdb_path} berhasil dikonversi ke folder {gdb_output_folder}")

        except Exception as e:
            print(f"❌ Gagal mengonversi {gdb_path}: {e}")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_gdb_to_shp_zip(input_folder, output_folder)
