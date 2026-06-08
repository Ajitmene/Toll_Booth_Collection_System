from UTILS.file_handler import read_file

SEARCH_VEHICLE = "FINAL_PROJECT/DATA/vehicles.json"

def search_vehicle():
    try :
        vehicle_no = input("Enter Vehicle No. ::").upper()
        
        search_file = read_file(SEARCH_VEHICLE)

        vehicle_found = None
        count = 0
        for vehicle in search_file :
            if vehicle["vehicle_no"] == vehicle_no :
                vehicle_found = vehicle
                count += 1

        if not vehicle_found :
            print("Vehicle Not Found....!!!")
            return
    
        print("\n======================= VEHICLE DETAILS =======================")
        print(f"{'Vehicle ID ::':<30} {vehicle['vehicle_no']:<40}")
        print(f"{'Vehicle Pass Count ::':<30} {count}")
        print(f"{'Owner Name ::':<30} {vehicle['owner_name']:<40}")
        print(f"{'Vehicle Type ::':<30} {vehicle['vehicle_type']:<40}")
        print(f"{'Date ::':<30} {vehicle['date']:<40}")
        time_only = vehicle_found['created_at'].split()[1]
        print(f"{'Time ::':<30} {time_only:<40}")

    
    except Exception as e :
        print(e)