from MODEL.toll import Toll_vehicle
from UTILS.file_handler import read_file , write_file
from UTILS.validators import validate_date

# Create file 
TOLL_VEHICLE_FILE = "FINAL_PROJECT/DATA/vehicles.json"

# Add vehicles in the file 
def add_vehicles():
    try :
        vehicle_no = input("Enter Vehicle No. ::").upper()
        owner_name = input("Enter Vehicle Owner name ::").title()
        print("\nVehicle Types")
        print("1. BIKE")
        print("2. CAR")
        print("3. BUS")
        print("4. TRUCK")

        choice = input("Enter vehicle type ::")

        vehicle_types = {
            "1" : "BIKE" ,
            "2" : "CAR" , 
            "3" : "BUS" ,
            "4" : "TRUCK"
        }
        vehicle_type = vehicle_types.get(choice)

        if not vehicle_type :
            print("Invalid Vehicle Type")
            return
        
        date = input("Enter Date (YYYY-MM-DD) ::")
        validate_date(date)
    
        vehicles = read_file(TOLL_VEHICLE_FILE)

            
        vehicle = Toll_vehicle(vehicle_no , owner_name , vehicle_type , date)
    
        vehicles.append(vehicle.to_dict())
        write_file(TOLL_VEHICLE_FILE , vehicles)

        print("Vehicle Added Successfully......")

# When my date in not valid format that this message will print 
    except ValueError as e :
        print("ERROR ::",e)        