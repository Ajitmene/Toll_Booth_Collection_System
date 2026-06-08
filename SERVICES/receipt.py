from datetime import datetime
from UTILS.file_handler import read_file , write_file

TOLL_VEHICLE_FILE = "FINAL_PROJECT/DATA/vehicles.json"
RECEIPT_FILE = "FINAL_PROJECT/DATA/receipt.json"

def generate_receipt():
    try :
        vehicle_no = input("Enter Vehicle No. ::").upper()
        
        vehicles = read_file(TOLL_VEHICLE_FILE)

        vehicle_found = None

        for vehicle in vehicles :
            if vehicle["vehicle_no"] == vehicle_no :
                vehicle_found = vehicle
                break

        if not vehicle_found :
            print("Vehicle Not Found....!!!")
            return
        

        vehicles_rates = {
            "BIKE" : 20 ,
            "CAR" : 100 ,
            "BUS" : 250 ,
            "TRUCK" : 350
        }

        amount = vehicles_rates.get(vehicle_found["vehicle_type"])


        receipts = read_file(RECEIPT_FILE)

        receipt = {
            "receipt_id" : f"REC{len(receipts)+1}",
            "vehicle_no" : vehicle_found["vehicle_no"],
            "owner_name" : vehicle_found["owner_name"],
            "vehicle_type" : vehicle_found["vehicle_type"],
            "amount" : amount ,
            "date" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        receipts.append(receipt)

        write_file(RECEIPT_FILE , receipts)

        print("\n" + "=" * 43)
        print(f"{'TOLL RECEIPT':^40}")
        print("=" * 43)

        print(f"{'Field':<30} {'Details':<40}")
        print("=" * 43)

        print(f"{'Receipt ID':<30} {receipt['receipt_id']:<40}")
        print(f"{'Vehicle No':<30} {receipt['vehicle_no']:<40}")
        print(f"{'Vehicle Owner Name':<30} {receipt['owner_name']:<40}")
        print(f"{'Vehicle Type':<30} {receipt['vehicle_type']:<40}")
        print(f"{'Amount':<30} ₹ {receipt['amount']:<38}")
        print(f"{'Date':<30} {receipt['date']:<40}")

        print("=" * 43)

    except Exception as e :
        print("ERROR ::",e)
