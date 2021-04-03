import pickle

def get_items():

    file_name = "item_dump.pkl"
    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list
