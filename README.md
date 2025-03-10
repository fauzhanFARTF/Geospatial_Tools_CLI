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
|   |-- input_coverage/           # Folder untuk input overlay (intersect, union, erase)
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
|-- .gitignore                     # File yang tidak perlu di-tracking oleh Git
|-- LICENSE
|-- README.md                      # Dokumentasi proyek
|-- setup.py                        # Setup script untuk instalasi paket
|-- pyproject.toml                  # Konfigurasi modern Python packaging
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
geospatial-tools --help
```

### Contoh Penggunaan
#### Konversi GDB ke SHP
```bash
geospatial-tools convert --input data/input/file.gdb --output data/output/file.shp
```

#### Transformasi ke WGS84
```bash
geospatial-tools transform --input data/input/file.shp --to WGS84 --output data/output/file_wgs84.shp
```

#### Melakukan Intersection
```bash
geospatial-tools analyze intersection --input data/input/file1.shp --overlay data/input_coverage/file2.shp --output data/output/intersection_result.shp
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
📩 Email: fn.fauzannurrachman@gmail.com  
📌 GitHub Issues: [Geospatial Tools CLI](https://github.com/fauzhanFARTF/geospatial-tools-cli/issues)

---

🚀 **Selamat menggunakan Geospatial Tools CLI!**