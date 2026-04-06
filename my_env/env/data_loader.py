import json
import os

def load_data():
    # get current file directory
    base_dir = os.path.dirname(__file__)
    
    # build path to emails.json
    path = os.path.join(base_dir, "data", "emails.json")
    
    with open(path, "r") as f:
        data = json.load(f)
    
    return data
