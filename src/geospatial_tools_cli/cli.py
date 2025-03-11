import os
import subprocess
from geospatial_tools_cli.utils.organizer import move_all_to_storage

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("\n========== Welcome to Geospatial Tools CLI ========== ")
        print("===== Please select the option you would like to perform. =====")
        print("1. Convert Data Type")
        print("2. Projection Transformation")
        print("3. Calculate Area")
        print("4. Analytics Tools")
        print("5. Move Input & Output Files to Storage 📦")
        print("6. Delete All Input & Output Data 🗑️")
        print("7. Remove Timestamp 🗑️")
        print("0. Exit 🚪")
        choice = input("Please Select: ")
        
        if choice == "1":
            convert_menu()
        elif choice == "2":
            projection_transformation_menu()
        elif choice == "3":
            calculate_area_menu()
        elif choice == "4":
            analytic_tools_menu()
        elif choice == "5":
            print("\n🔄 Processing Move All to Storage...\n")
            result = move_all_to_storage()
            print(result)
            input("\n⏎ Press Enter to return...")  
        elif choice == "7":
            print("\n🔄 Processing Remove Timestamp...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/utils/remove_timestamp.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  
        elif choice == "0":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid option, please try again.")

def convert_menu():
    while True:
        clear_screen()
        print("\n========= Convert Data Type =========")
        print("========= Select Data Source =========")
        print("1. From GDB")
        print("2. From SHP")
        print("3. From GeoJSON")
        print("4. From KML")
        print("0. Return to Main Menu 🔙")
        choice = input("Please Select: ")
        
        if choice == "1":
            convert_gdb()
        elif choice == "2":
            convert_shp()
        elif choice == "3":
            convert_geojson()
        elif choice == "4":
            convert_kml()
        elif choice == "0":
            break
        else:
            print("Invalid option, please try again.")

def projection_transformation_menu():
    while True:
        clear_screen()
        print("\n============ Projection Transformation ===========")
        print("=========== Select Transformation Option ===========")
        print("1. Transformation to WGS84")
        print("2. Transformation to UTM")
        print("3. Transformation to TM3")
        print("4. Check Projection")
        print("0. Return to Main Menu 🔙")
        choice = input("Please Select: ")
        
        if choice == "0":
            break
        if choice == "4":
            print("\n🔄 Processing Check Projection...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/projection_transformation/check_projection.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        else:
            print("Processing transformation...")

def calculate_area_menu():
    while True:
        clear_screen()
        print("\n============ Calculate Area ===========")
        print("=========== Select Option ===========")
        print("1. Calculate Area")
        print("2. Area Adjustment -> Export")
        print("0. Return to Main Menu 🔙")
        choice = input("Please Select: ")
        
        if choice == "0":
            break
        else:
            print("Processing area calculation...")

def analytic_tools_menu():
    while True:
        clear_screen()
        print("\n============ Analytic Tools ===========")
        print("=========== Select Option ===========")
        print("1. Intersect")
        print("2. Union")
        print("3. Erase")
        print("4. Merge Excel")
        print("0. Return to Main Menu 🔙")
        choice = input("Please Select: ")

        if choice == "1":
            print("\n🔄 Processing Intersect...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/analytic/intersection.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang          
        if choice == "2":
            print("\n🔄 Processing Union...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/analytic/union.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang          
        if choice == "3":
            print("\n🔄 Processing Erase...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/analytic/erase.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang          
        if choice == "4":
            print("\n🔄 Processing Erase...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/analytic/merge_excel.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang          
        if choice == "0":
            break
        else:
            print("Processing analytic tool...")

def convert_gdb():
    while True:
        clear_screen()
        print("\n======== Convert Data Type ========")
        print("===== Select Conversion Option =====")
        print("1. GDB → KML")
        print("2. GDB → GeoJSON")
        print("3. GDB → SHP")
        print("4. GDB → SHP & ZIP")
        print("0. Back  🔙")
        choice = input("Please Select: ")
        if choice == "1":
            print("\n🔄 Processing conversion GDB to KML...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/gdb_to_kml.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang  
        if choice == "2":
            print("\n🔄 Processing conversion GDB to GeoJSON...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/gdb_to_geojson.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang  
        if choice == "3":
            print("\n🔄 Processing conversion GDB to SHP...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/gdb_to_shp.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "4":
            print("\n🔄 Processing conversion GDB to SHP & ZIP...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/gdb_to_shp_zip.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang         
        if choice == "0":
            break
        else:
            print("Processing conversion...")

def convert_shp():
    while True:
        clear_screen()
        print("\n======== Convert Data Type ========")
        print("===== Select Conversion Option =====")
        print("1. SHP → KML")
        print("2. SHP → GeoJSON")
        print("0. Back  🔙")
        choice = input("Please Select: ")
        
        if choice == "1":
            print("\n🔄 Processing conversion SHP to KML...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/shp_to_kml.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "2":
            print("\n🔄 Processing conversion SHP to GeoJSON...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/shp_to_geojson.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "0":
            break
        else:
            print("Processing conversion...")

def convert_geojson():
    while True:
        clear_screen()
        print("\n======== Convert Data Type ========")
        print("===== Select Conversion Option =====")
        print("1. GeoJSON → KML")
        print("2. GeoJSON → SHP")
        print("3. GeoJSON → SHP & ZIP")
        print("4. GeoJSON → CSV")
        print("0. Back  🔙")
        choice = input("Please Select: ")

        if choice == "1":
            print("\n🔄 Processing conversion GeoJSON to KML...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/geojson_to_kml.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang     
        if choice == "2":
            print("\n🔄 Processing conversion GeoJSON to SHP...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/geojson_to_shp.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "3":
            print("\n🔄 Processing conversion GeoJSON to SHP & ZIP...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/geojson_to_shp_zip.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "4":
            print("\n🔄 Processing conversion GeoJSON to CSV...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/geojson_to_csv.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "0":
            break
        else:
            print("Processing conversion...")

def convert_kml():
    while True:
        clear_screen()
        print("\n======== Convert Data Type ========")
        print("===== Select Conversion Option =====")
        print("1. KML → GeoJSON")
        print("2. KML → SHP")
        print("3. KML → SHP & ZIP")
        print("0. Back  🔙")
        choice = input("Please Select: ")
        if choice == "1":
            print("\n🔄 Processing conversion KML to GeoJSON...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/kml_to_geojson.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang          
        if choice == "2":
            print("\n🔄 Processing conversion KML to SHP...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/kml_to_shp.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang    
        if choice == "3":
            print("\n🔄 Processing conversion KML to SHP & ZIP...\n")
            subprocess.run(["python", "src/geospatial_tools_cli/converters/kml_to_shp_zip.py"], capture_output=False)
            input("\n⏎ Press Enter to return...")  # Agar output tidak langsung hilang         
        if choice == "0":
            break
        else:
            print("Processing conversion...")

if __name__ == "__main__":
    main()
