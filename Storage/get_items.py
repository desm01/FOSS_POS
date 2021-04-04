import pickle
from Storage.store_items import default_store_items

def get_items():
    try:
        file_name = "item_dump.pkl"
        open_file = open(file_name, "rb")
        loaded_list = pickle.load(open_file)
        open_file.close()
        return loaded_list
    except:
        default_store_items()
        get_items()

