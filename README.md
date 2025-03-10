# Geospatial Tools CLI

Geospatial Tools CLI adalah aplikasi Command-Line Interface (CLI) untuk melakukan berbagai operasi geospasial, termasuk konversi format, transformasi proyeksi, analisis spasial, dan perhitungan geospasial.

## 📌 Fitur Utama
- **Konversi format geospasial** (GDB, SHP, GeoJSON, KML, ZIP)
- **Transformasi proyeksi** (WGS84, UTM, TM3)
- **Analisis spasial** (Intersection, Union, Erase)
- **Perhitungan area geospasial**
- **Logging otomatis untuk setiap proses**
- **Dapat dijalankan melalui terminal atau shell**

---

## 📂 Struktur Folder
```bash
geospatial_tools_cli/
|-- env/                          # Virtual environment (tambahkan ke .gitignore)
|-- build/                        # Direktori build (jika diperlukan)
|-- data/                         
|   |-- input/                    # Folder untuk file input geospasial
|   |-- input_coverage/            # Folder untuk input coverage (intersect, union, erase)
|   |-- output/                   # Folder untuk hasil transformasi
|   |-- storage/                  # Penyimpanan file hasil transformasi yang telah diorganisir
|       |-- gdb/
|       |-- geojson/
|       |-- kml/
|       |-- shp/
|       |-- zip/
|-- logs/                         # Folder menyimpan log proses transformasi
|-- src/                          # Folder utama kode sumber
|   |-- geospatial_tools_cli/      # Package utama CLI
|   |   |-- __init__.py
|   |   |-- cli.py                 # Entry point CLI
|   |   |-- converters/            # Modul konversi format geospasial
|   |   |-- projection_transformation/  # Modul transformasi proyeksi
|   |   |-- analytic/               # Modul analisis spasial
|   |   |-- calculation/            # Modul perhitungan geospasial
|   |   |-- utils/                   # Modul utilitas
|-- tests/                        # Direktori pengujian
|-- requirements.txt               # Daftar dependensi Python
|-- .gitignore                      # File yang tidak perlu di-tracking oleh Git
|-- .gitattributes                   # Atribut khusus Git
|-- LICENSE
|-- README.md                       # Dokumentasi proyek
|-- setup.py                         # Setup script untuk instalasi paket
|-- pyproject.toml                   # Konfigurasi modern Python packaging
```

---

## 🚀 Instalasi
### 1. Buat dan Aktifkan Virtual Environment
```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 2. Instal Dependensi
```bash
pip install -r requirements.txt
```

### 3. Instal Paket sebagai CLI (Opsional)
```bash
pip install .
```

Setelah instalasi, CLI dapat dijalankan dengan perintah:
```bash
geospatial-tools --help
```

---

## 🛠️ Cara Penggunaan
### Menampilkan Bantuan
```bash
python -m geospatial_tools_cli.cli --help
```

### Menu Utama CLI
```bash
========== Welcome to Geospatial Tools CLI ========== 
===== Please select the option you would like to perform. =====
1. Convert Data Type
2. Projection Transformation
3. Calculate Area
4. Analytics Tools
5. Move Input & Output Files to Storage 📦
6. Delete All Input & Output Data 🗑️
7. Remove Timestamp 🗑️
0. Exit 🚪
Please Select: 
```

### Convert Data Type
```bash
========= Convert Data Type =========
========= Select Data Source =========
1. From GDB
2. From SHP
3. From GeoJSON
4. From KML
0. Return to Main Menu 🔙
Please Select: 
```

#### Opsi Konversi
```bash
======== Convert Data Type ========
===== Select Conversion Option =====
1. GDB → KML
2. GDB → GeoJSON
3. GDB → SHP
4. GDB → SHP & ZIP
0. Back 🔙
Please Select: 
```
```bash
======== Convert Data Type ========
===== Select Conversion Option =====
1. SHP → KML
2. SHP → GeoJSON
0. Back 🔙
Please Select: 
```
```bash
======== Convert Data Type ========
===== Select Conversion Option =====
1. GeoJSON → KML
2. GeoJSON → SHP
3. GeoJSON → SHP & ZIP
0. Back 🔙
Please Select: 
```
```bash
======== Convert Data Type ========
===== Select Conversion Option =====
1. KML → GeoJSON
2. KML → SHP
3. KML → SHP & ZIP
0. Back 🔙
Please Select: 
```

### Projection Transformation
```bash
============ Projection Transformation ===========
=========== Select Transformation Option ===========
1. Transformation to WGS84
2. Transformation to UTM
3. Transformation to TM3
4. Check Projection
0. Return to Main Menu 🔙
Please Select: 
```

### Calculate Area
```bash
============ Calculate Area ===========
=========== Select Option ===========
1. Calculate Area
2. Area Adjustment -> Export
0. Return to Main Menu 🔙
Please Select: 
```

### Analytic Tools
```bash
============ Analytic Tools ===========
=========== Select Option ===========
1. Intersect
2. Union
3. Erase
0. Return to Main Menu 🔙
Please Select: 
```

---

## 🧪 Pengujian
Jalankan tes unit dengan pytest:
```bash
pytest tests/
```

---

## 📝 Lisensi
Proyek ini dilisensikan di bawah **MIT License**.

---

## 📧 Kontribusi
1. Fork repository ini
2. Buat branch baru (`git checkout -b feature-branch`)
3. Commit perubahan (`git commit -m 'Add new feature'`)
4. Push ke branch (`git push origin feature-branch`)
5. Ajukan Pull Request

---

## 📌 Kontak
Untuk pertanyaan atau masalah, silakan hubungi:
📩 Email: [fn.fauzannurrachman@gmail.com]
📌 GitHub Issues: [Geospatial Tools CLI](https://github.com/fauzhanFARTF/geospatial-tools-cli/issues)

---

🚀 **Selamat menggunakan Geospatial Tools CLI!**

