import json
import os

def read_file(path):
    if not os.path.exists(path):
        return []
    
    try :
        with open(path , "r") as f :
            return json.load(f)
    
    except json.JSONDecodeError :
        print("Warning : JSON file is empty or corrupted resetting file...!")
        return[]
    

def write_file(path , data) :

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path , "w") as f :
        json.dump(data , f , indent=4)
