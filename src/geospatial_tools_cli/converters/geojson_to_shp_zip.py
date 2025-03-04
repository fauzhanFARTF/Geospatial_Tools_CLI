import geopandas as gpd
import os
import glob
import zipfile

# Dapatkan path absolut dari direktori proyek
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

# Path input dan output
input_folder = os.path.join(BASE_DIR, "data/input")
output_folder = os.path.join(BASE_DIR, "data/output")

def convert_geojson_to_shp_zip(input_folder, output_folder):
    """
    Mengonversi semua file GeoJSON dalam folder input ke format Shapefile (SHP),
    menyimpannya dalam folder berdasarkan nama file, dan mengompresnya ke ZIP.

    :param input_folder: Path folder yang berisi file GeoJSON
    :param output_folder: Path folder untuk menyimpan file SHP dan ZIP
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output ada

    # Cari semua file GeoJSON dalam folder input
    geojson_files = glob.glob(os.path.join(input_folder, "*.geojson"))

    if not geojson_files:
        print(f"❌ Tidak ada file GeoJSON di folder input: {input_folder}")
        return

    for geojson_file in geojson_files:
        try:
            # Ambil nama file tanpa ekstensi
            filename = os.path.splitext(os.path.basename(geojson_file))[0]
            
            # Buat folder berdasarkan nama file input
            folder_output = os.path.join(output_folder, filename)
            os.makedirs(folder_output, exist_ok=True)

            # Path untuk output SHP
            output_shp = os.path.join(folder_output, f"{filename}.shp")
            
            # Baca GeoJSON dan konversi ke SHP
            gdf = gpd.read_file(geojson_file)
            gdf.to_file(output_shp, driver="ESRI Shapefile")

            # Buat file ZIP
            zip_filename = os.path.join(output_folder, f"{filename}.zip")
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for shp_file in glob.glob(os.path.join(folder_output, f"{filename}.*")):
                    zipf.write(shp_file, os.path.relpath(shp_file, output_folder))

            print(f"✅ {geojson_file} berhasil dikonversi ke {zip_filename}")
        
        except Exception as e:
            print(f"❌ Gagal mengonversi {geojson_file}: {e}")

if __name__ == "__main__":
    print(f"📂 Input Folder: {input_folder}")
    print(f"📂 Output Folder: {output_folder}\n")

    convert_geojson_to_shp_zip(input_folder, output_folder)
