import os
import re
from pathlib import Path
import shutil

def rename_and_copy_files(source_directory, destination_directory):
    """Menghapus timestamp dan ekstensi jenis (_GeoJSON, _kml, _shp) dari nama file dan folder, lalu menyalinnya ke folder tujuan."""
    pattern = re.compile(r"(_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})|(_GeoJSON|_kml|_shp)")
    destination_directory = Path(destination_directory)
    destination_directory.mkdir(parents=True, exist_ok=True)  # Buat folder tujuan jika belum ada

    for file_path in Path(source_directory).rglob("*"):
        relative_path = file_path.relative_to(source_directory)
        new_relative_path = Path(pattern.sub("", str(relative_path)))  # Hapus timestamp dan ekstensi jenis dari path relatif
        new_path = destination_directory / new_relative_path  # Path baru di folder tujuan

        if file_path.is_dir():
            new_path.mkdir(parents=True, exist_ok=True)  # Buat folder baru jika belum ada
        elif file_path.is_file():
            new_path.parent.mkdir(parents=True, exist_ok=True)  # Pastikan folder tujuan ada
            shutil.copy2(file_path, new_path)  # Salin file ke lokasi baru
            print(f"✅ Copied and Renamed: {file_path} -> {new_path}")


def main():
    BASE_DIR = Path(__file__).resolve().parents[3]
    input_folder = BASE_DIR / "data/input"
    output_folder = BASE_DIR / "data/output"
    
    if not input_folder.exists():
        print(f"⚠️ Folder {input_folder} tidak ditemukan.")
        exit(1)
    
    print(f"📂 Processing files from: {input_folder}\n")
    rename_and_copy_files(input_folder, output_folder)

if __name__ == "__main__":
    main()
