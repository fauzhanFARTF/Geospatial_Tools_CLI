import geopandas as gpd
import os
import glob

def convert_geojson_to_shp(input_folder, output_folder):
    """
    Mengonversi semua file GeoJSON dalam folder input ke format Shapefile (SHP).
    
    :param input_folder: Path folder yang berisi file GeoJSON
    :param output_folder: Path folder untuk menyimpan file SHP
    """
    os.makedirs(output_folder, exist_ok=True)  # Pastikan folder output tersedia

    # Dapatkan semua file GeoJSON dalam folder input
    geojson_files = glob.glob(os.path.join(input_folder, "*.geojson"))

    if not geojson_files:
        print("❌ Tidak ada file GeoJSON di folder input!")
        return

    for geojson_file in geojson_files:
        try:
            # Ambil nama file tanpa ekstensi
            filename = os.path.splitext(os.path.basename(geojson_file))[0]
            
            # Path untuk output SHP
            output_shp = os.path.join(output_folder, f"{filename}.shp")
            
            # Baca GeoJSON
            gdf = gpd.read_file(geojson_file)
            
            # Simpan sebagai SHP
            gdf.to_file(output_shp, driver="ESRI Shapefile")

            print(f"✅ {geojson_file} berhasil dikonversi ke {output_shp}")
        
        except Exception as e:
            print(f"❌ Gagal mengonversi {geojson_file}: {e}")

if __name__ == "__main__":
    input_folder = "/Users/fauzannurrachman/Sites/Project/Portofolio/tools/Geospatial_Tools_CLI/data/input"    # Folder input yang berisi file GeoJSON
    output_folder = "/Users/fauzannurrachman/Sites/Project/Portofolio/tools/Geospatial_Tools_CLI/data/output"  # Folder output untuk hasil SHP

    convert_geojson_to_shp(input_folder, output_folder)
