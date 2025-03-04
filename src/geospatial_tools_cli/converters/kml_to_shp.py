import geopandas as gpd
import os
import glob
import zipfile

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_kml_to_shp_zip(input_folder, output_folder):
    """
    Mengonversi semua file KML dalam folder input ke format Shapefile (SHP),
    menyimpannya dalam folder berdasarkan nama file, dan mengompresnya ke ZIP.

    :param input_folder: Path folder yang berisi file KML
    :param output_folder: Path folder untuk menyimpan file SHP dan ZIP
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Cari semua file KML dalam folder input
    kml_files = glob.glob(os.path.join(input_folder, "*.kml"))

    if not kml_files:
        print(f"❌ Tidak ada file KML di folder input: {input_folder}")
        return

    for kml_file in kml_files:
        try:
            # Ambil nama file tanpa ekstensi
            filename = os.path.splitext(os.path.basename(kml_file))[0]
            
            # Buat folder berdasarkan nama file input
            folder_output = os.path.join(output_folder, filename)
            os.makedirs(folder_output, exist_ok=True)

            # Path untuk output SHP
            output_shp = os.path.join(folder_output, f"{filename}.shp")
            
            # Baca KML dan konversi ke SHP
            gdf = gpd.read_file(kml_file)
            gdf.to_file(output_shp, driver="ESRI Shapefile")
        
        except Exception as e:
            print(f"❌ Gagal mengonversi {kml_file}: {e}")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_kml_to_shp_zip(input_folder, output_folder)
