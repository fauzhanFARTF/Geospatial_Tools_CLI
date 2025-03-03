import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
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
        print("0. Exit 🚪")
        choice = input("Please Select: ")
        
        if choice == "1":
            convert_menu()
        elif choice == "2":
            projection_transformation_menu()
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
        else:
            print("Processing transformation...")

def convert_gdb():
    while True:
        clear_screen()
        print("\n======== Convert Data Type ========")
        print("===== Select Conversion Option =====")
        print("1. GDB → KML")
        print("2. GDB → GeoJSON")
        print("3. GDB → SHP")
        print("4. GDB → SHP & ZIP")
        print("5. Back  🔙")
        choice = input("Please Select: ")
        
        if choice == "5":
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
        print("3. Back  🔙")
        choice = input("Please Select: ")
        
        if choice == "3":
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
        print("4. Back  🔙")
        choice = input("Please Select: ")
        
        if choice == "4":
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
        print("4. Back  🔙")
        choice = input("Please Select: ")
        
        if choice == "4":
            break
        else:
            print("Processing conversion...")

if __name__ == "__main__":
    main_menu()