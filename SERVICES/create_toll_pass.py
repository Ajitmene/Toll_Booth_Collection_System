from datetime import datetime, timedelta
from UTILS.file_handler import read_file, write_file


PASS_FILE = "FINAL_PROJECT/DATA/passes.json"
VEHICLE_FILE = "FINAL_PROJECT/DATA/vehicles.json"


def create_pass():

    vehicle_no = input("Enter Vehicle Number: ").upper()

    vehicles = read_file(VEHICLE_FILE)
    passes = read_file(PASS_FILE)

    vehicle = None

    # Search Vehicle
    for v in vehicles:
        if v["vehicle_no"] == vehicle_no:
            vehicle = v
            break

    if not vehicle:
        print("Vehicle Not Found")
        return

    # Check Existing Active Pass
    for existing_pass in passes:

        if existing_pass["vehicle_no"] == vehicle_no:

            valid_date = datetime.strptime(
                existing_pass["valid_till"],
                "%d-%m-%Y"
            )

            if valid_date >= datetime.now():

                print("\nPass Already Active")
                print(
                    "Valid Till ::",
                    existing_pass["valid_till"]
                )
                return

    print("\n===== PASS TYPES =====")
    print("1. Monthly Pass")
    print("2. Yearly Pass")

    choice = input("Choose Pass Type :: ")

    if choice == "1":
        pass_type = "Monthly"
        valid_till = datetime.now() + timedelta(days=30)

    elif choice == "2":
        pass_type = "Yearly"
        valid_till = datetime.now() + timedelta(days=365)

    else:
        print("Invalid Choice")
        return

    toll_pass = {
        "pass_id": f"PASS{len(passes)+1}",
        "vehicle_no": vehicle_no,
        "owner_name": vehicle["owner_name"],
        "vehicle_type": vehicle["vehicle_type"],
        "pass_type": pass_type,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "valid_till": valid_till.strftime(
            "%d-%m-%Y"
        )
    }

    passes.append(toll_pass)

    write_file(PASS_FILE, passes)

    print("\n" + "=" * 45)
    print(f"{'PASS CREATED SUCCESSFULLY':^45}")
    print("=" * 45)
    print(f"Pass ID      : {toll_pass['pass_id']}")
    print(f"Vehicle No   : {toll_pass['vehicle_no']}")
    print(f"Owner Name   : {toll_pass['owner_name']}")
    print(f"Vehicle Type : {toll_pass['vehicle_type']}")
    print(f"Pass Type    : {toll_pass['pass_type']}")
    print(f"Valid Till   : {toll_pass['valid_till']}")
    print("=" * 45)