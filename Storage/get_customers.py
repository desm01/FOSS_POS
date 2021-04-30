import pickle

def get_customers():

    file_name = "customer_dump.pkl"
    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list
