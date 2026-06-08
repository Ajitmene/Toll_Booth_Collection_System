# from MODEL.toll import Toll_vehicle
from SERVICES.add_vehicle import add_vehicles
from SERVICES.receipt import generate_receipt
from SERVICES.view_receipts import view_receipts
from SERVICES.search_vehicle import search_vehicle
from SERVICES.revenue_report import revenue_report
from SERVICES.create_toll_pass import create_pass
from SERVICES.search_pass import search_pass



def menu():
    while True :
        print("\n=================== TOLL BOOTH COLLECTION =====================")
        print("1. ADD VEHICLE WITH VEHICLE TYPE")
        print("2. GENERATE RECEIPT")
        print("3. VIEW RECEIPT")
        print("4. SEARCH VEHICLE DETAILS")
        print("5. REVENUE REPORTS")
        print("6. CREATE TOOL PASS")
        print("7. SEARCH PASS")
        print("8. EXIT")

        choice = input("Enter Choice ::")

        if choice == "1" :
            add_vehicles()
        elif choice == "2" :
            generate_receipt()
        elif choice == "3" :
            view_receipts()
        elif choice == "4" :
            search_vehicle()
        elif choice == "5" :
            revenue_report()
        elif choice == "6" :
            create_pass()
        elif choice == "7" :
            search_pass()
        elif choice == "8" :
            print("THANKU FOR VISITING...........!!!")
            break
        else :
            print("Invalid Choice...!")

if __name__ == "__main__":
    menu()   