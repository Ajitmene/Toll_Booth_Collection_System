from UTILS.file_handler import read_file
from datetime import datetime, timedelta


def revenue_report():

    reports = read_file("FINAL_PROJECT/DATA/receipt.json")

    if not reports:
        print("No Receipt Data Found...")
        return

    print("\n============= REVENUE REPORTS =============")
    print("1. TODAYS REVENUE")
    print("2. WEEKLY REVENUE")
    print("3. MONTHLY REVENUE")
    print("4. THREE MONTHS REVENUE")

    choice = input("Enter Choice :: ")

    today = datetime.now()

    if choice == "1":
        start_date = today - timedelta(days=1)
        title = "Today's Revenue"

    elif choice == "2":
        start_date = today - timedelta(days=7)
        title = "Weekly Revenue"

    elif choice == "3":
        start_date = today - timedelta(days=30)
        title = "Monthly Revenue"

    elif choice == "4":
        start_date = today - timedelta(days=90)
        title = "Three Months Revenue"

    else:
        print("Invalid Choice")
        return

    total_revenue = 0
    total_vehicles = 0

    for report in reports:

        receipt_date = datetime.strptime(
            report["date"],
            "%Y-%m-%d %H:%M:%S"   # fixed format
        )

        if receipt_date >= start_date:
            total_revenue += report["amount"]
            total_vehicles += 1

    print("\n" + "=" * 45)
    print(f"{title:^45}")
    print("=" * 45)
    print(f"Total Vehicles Passed : {total_vehicles}")
    print(f"Total Revenue         : ₹ {total_revenue}")
    print("=" * 45)