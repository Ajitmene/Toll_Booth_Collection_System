from UTILS.file_handler import read_file

RECEIPT_FILE = "FINAL_PROJECT/DATA/receipt.json"

def view_receipts():
    view_file = read_file(RECEIPT_FILE)

    if not view_file :
        print("No Receipts Founds")
        return
    
    print("\n====================== ALL RECEIPTS ======================")
    for  receipt in view_file :
        print("\n")
        print("-"*60)
        print(f"{'Receipt ID':<30} {receipt['receipt_id']:<40}")
        print(f"{'Vehicle No':<30} {receipt['vehicle_no']:<40}")
        print(f"{'Vehicle Owner Name':<30} {receipt['owner_name']:<40}")
        print(f"{'Vehicle Type':<30} {receipt['vehicle_type']:<40}")
        print(f"{'Amount':<30} ₹ {receipt['amount']:<38}")
        print(f"{'Date':<30} {receipt['date']:<40}")
        print("-"*60)