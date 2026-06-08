from datetime import datetime
from UTILS.file_handler import read_file


PASS_FILE = "FINAL_PROJECT/DATA/passes.json"


def search_pass():

    vehicle_no = input(
        "Enter Vehicle Number :: "
    ).upper()

    passes = read_file(PASS_FILE)

    found = False

    for toll_pass in passes:

        if toll_pass["vehicle_no"] == vehicle_no:

            valid_till = datetime.strptime(
                toll_pass["valid_till"],
                "%d-%m-%Y"
            )

            # Check pass status
            if valid_till >= datetime.now():
                status = "ACTIVE"
            else:
                status = "EXPIRED"

            print("\n" + "=" * 45)
            print(f"{'PASS DETAILS':^45}")
            print("=" * 45)

            print(
                f"{'Pass ID':<20}"
                f": {toll_pass['pass_id']}"
            )

            print(
                f"{'Vehicle No':<20}"
                f": {toll_pass['vehicle_no']}"
            )

            print(
                f"{'Owner Name':<20}"
                f": {toll_pass['owner_name']}"
            )

            print(
                f"{'Vehicle Type':<20}"
                f": {toll_pass['vehicle_type']}"
            )

            print(
                f"{'Pass Type':<20}"
                f": {toll_pass['pass_type']}"
            )

            print(
                f"{'Valid Till':<20}"
                f": {toll_pass['valid_till']}"
            )

            print(
                f"{'Status':<20}"
                f": {status}"
            )

            print("=" * 45)

            found = True
            break

    if not found:
        print("Pass Not Found")