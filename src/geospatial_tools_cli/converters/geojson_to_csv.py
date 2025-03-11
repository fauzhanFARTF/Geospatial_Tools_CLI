import json
import csv
import geopandas as gpd
from shapely.geometry import shape
from pathlib import Path
from datetime import datetime

def geojson_to_csv(input_folder, output_folder):
    """Mengonversi semua file GeoJSON (termasuk di subfolder) ke CSV dengan koordinat titik tengah dan timestamp."""

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    input_folder = Path(input_folder)
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)  # Buat folder output jika belum ada

    # Cari semua file .geojson dalam folder utama & subfolder
    geojson_files = list(input_folder.rglob("*.geojson"))

    if not geojson_files:
        raise FileNotFoundError(f"⚠️ Tidak ada file GeoJSON ditemukan di {input_folder}.")

    for geojson_file in geojson_files:
        print(f"📂 Memproses file: {geojson_file}")

        with open(geojson_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        if "features" not in data:
            print(f"⚠️ {geojson_file.name} tidak memiliki fitur, dilewati.")
            continue

        # Ambil semua kolom atribut yang tersedia
        all_keys = set()
        for feature in data["features"]:
            all_keys.update(feature.get("properties", {}).keys())

        all_keys = sorted(all_keys)  # Urutkan kolom agar rapi

        # Tambahkan kolom untuk ID, Geometry Type, dan Koordinat Centroid
        header = ["ID"] + list(all_keys) + ["Geometry Type", "Centroid Longitude", "Centroid Latitude"]

        # Buat nama file dengan timestamp & struktur subfolder yang sama
        relative_path = geojson_file.relative_to(input_folder)  # Menjaga struktur subfolder
        parts = list(relative_path.parts)

        # Tambahkan timestamp ke setiap bagian folder kecuali nama file
        new_parts = [f"{part}_{timestamp}_csv" for part in parts[:-1]]
        new_parts.append(parts[-1].replace(".geojson", f"_{timestamp}.csv"))

        output_csv = output_folder / Path(*new_parts)
        output_csv.parent.mkdir(parents=True, exist_ok=True)  # Buat subfolder jika perlu

        with open(output_csv, "w", encoding="utf-8", newline="") as csv_file:
            writer = csv.writer(csv_file)
            
            # Tulis header
            writer.writerow(header)

            # Tulis data fitur
            for i, feature in enumerate(data["features"], start=1):
                properties = feature.get("properties", {})
                geometry = feature.get("geometry", {})
                geometry_type = geometry.get("type", "Unknown")

                # Hitung titik tengah (centroid)
                try:
                    geom = shape(geometry)
                    centroid = geom.centroid
                    centroid_lon, centroid_lat = centroid.x, centroid.y
                except Exception:
                    centroid_lon, centroid_lat = "N/A", "N/A"

                row_values = [i] + [properties.get(key, "-") for key in all_keys] + [geometry_type, centroid_lon, centroid_lat]
                writer.writerow(row_values)

        print(f"✅ Hasil konversi disimpan di: {output_csv}")

def main():
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_folder = BASE_DIR / "data/input"
    output_folder = BASE_DIR / "data/output"

    print("✅ Memulai konversi GeoJSON ke CSV...\n")
    geojson_to_csv(input_folder, output_folder)
    print("\n🎉 Semua file berhasil dikonversi!")

if __name__ == "__main__":
    main()
