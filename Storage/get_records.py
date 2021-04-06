import pickle
#from Storage.store_records import record_transaction

def get_records():

    file_name = "records_dump.pkl"
    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list
