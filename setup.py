from setuptools import setup, find_packages

setup(
    name="geospatial_tools_cli",
    version="1.0",
    packages=find_packages(include=["src", "src.*"]),  # Pastikan src dikenali
    entry_points={
        "console_scripts": [
            "geos_tools_cli=src.main:main"  # Pastikan src.main dideklarasikan
        ]
    },
    install_requires=[
        "fiona==1.10.1",
        "geopandas==1.0.1",
        "pyshp==2.3.1",
        "pyproj==3.7.0",
        "gdal==3.10.1",
        "setuptools==75.8.0"
    ]
)
