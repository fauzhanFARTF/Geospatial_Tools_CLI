from setuptools import setup, find_packages

setup(
    name="geospatial_tools_cli",
    version="1.0",
    description="Geospatial Tools CLI for processing spatial data",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "geos_tools_cli=geospatial_tools_cli.cli:main"  # Sesuaikan path ke fungsi main
        ]
    },
    install_requires=[
        "fiona==1.10.1",
        "geopandas==1.0.1",
        "pyshp==2.3.1",
        "pyproj==3.7.0",
        "gdal==3.10.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
