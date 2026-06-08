from datetime import datetime

class Toll_vehicle:
    def __init__(self , vehicle_no , owner_name , vehicle_type , date ):
        self.vehicle_no = vehicle_no
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type
        self.date = date
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

    def to_dict(self):
        return self.__dict__
    