import pickle
from Storage.store_staff import default_store_staff

def get_staff():
    try:
        file_name = "staff_dump.pkl"
        open_file = open(file_name, "rb")
        loaded_list = pickle.load(open_file)
        open_file.close()
        return loaded_list
    except:
        default_store_staff()
        get_staff()

