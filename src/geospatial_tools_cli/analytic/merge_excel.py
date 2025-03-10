import os
import datetime
from pathlib import Path
import geopandas as gpd
import pandas as pd

def find_geospatial_file(file_path):
    """Memeriksa apakah file geospasial (GeoJSON, KML, SHP) tersedia."""
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"❌ File {file_path} tidak ditemukan!")

    supported_formats = {".geojson", ".kml", ".shp"}
    
    if file_path.suffix.lower() not in supported_formats:
        raise ValueError(f"❌ Format {file_path.suffix} tidak didukung! Harap gunakan GeoJSON, KML, atau SHP.")

    return file_path

def find_excel_file(file_path):
    """Memeriksa apakah file Excel tersedia."""
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"❌ File Excel {file_path} tidak ditemukan!")

    if file_path.suffix.lower() not in {".xls", ".xlsx"}:
        raise ValueError(f"❌ Format {file_path.suffix} tidak didukung! Harap gunakan .xls atau .xlsx.")

    return file_path

def merge_geospatial_with_excel(input_geo_file, input_excel_file, output_folder, join_column):
    """Menggabungkan data geospasial dengan file Excel berdasarkan kolom tertentu."""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    input_geo_file = find_geospatial_file(input_geo_file)
    input_excel_file = find_excel_file(input_excel_file)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"🔄 Processing merge: {input_geo_file.name} ⨝ {input_excel_file.name}...")

    try:
        # Baca data geospasial
        gdf_input = gpd.read_file(input_geo_file)

        if join_column not in gdf_input.columns:
            raise ValueError(f"❌ Kolom '{join_column}' tidak ditemukan dalam file geospasial!")

        print(f"📌 {input_geo_file.name} memiliki {len(gdf_input)} fitur.")
        print(f"📊 Kolom dalam Geospatial: {gdf_input.columns.tolist()}")

        # Baca data Excel
        df_excel = pd.read_excel(input_excel_file)

        if join_column not in df_excel.columns:
            raise ValueError(f"❌ Kolom '{join_column}' tidak ditemukan dalam file Excel!")

        print(f"📊 Kolom dalam Excel: {df_excel.columns.tolist()}")

        # Merge data geospasial dengan Excel
        print("🚀 Melakukan penggabungan data...")
        merged_gdf = gdf_input.merge(df_excel, on=join_column, how='left')

        # Jika ada kolom baru, pastikan nilai NaN diganti dengan string kosong atau nilai default
        merged_gdf.fillna("", inplace=True)

        if merged_gdf.empty:
            print(f"⚠️ Hasil merge kosong untuk {input_geo_file.name}!")
            return

        print(f"✅ Hasil merge memiliki {len(merged_gdf)} fitur.")
        print(f"📊 Kolom setelah merge: {merged_gdf.columns.tolist()}")

        # Tentukan format output berdasarkan format input
        output_extension = input_geo_file.suffix.lower()
        output_driver = {
            ".shp": "ESRI Shapefile",
            ".kml": "KML",
            ".geojson": "GeoJSON"
        }.get(output_extension, "GeoJSON")

        output_file = output_folder / f"{input_geo_file.stem}_merged{output_extension}"
        merged_gdf.to_file(output_file, driver=output_driver)
        print(f"✅ Hasil merge disimpan di: {output_file}")

    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_geo_file = BASE_DIR / "data/input/mydata.geojson"
    input_excel_file = BASE_DIR / "data/input_coverage/data.xlsx"
    output_folder = BASE_DIR / "data/output"
    join_column = "id"  # Sesuaikan dengan kolom yang menjadi key untuk merge

    print("✅ Memulai proses merge...")
    merge_geospatial_with_excel(input_geo_file, input_excel_file, output_folder, join_column)
    print("🎉 Proses merge selesai!")
