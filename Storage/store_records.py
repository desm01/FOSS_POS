
from Storage.get_records import get_records 
import pickle

def record_transaction(transaction):

    try:
        list_of_transactions = get_records()
    except:
        list_of_transactions = []
        

    file_name = "records_dump.pkl"
    open_file = open(file_name, "wb")
    
    list_of_transactions.append(transaction)
    pickle.dump(list_of_transactions, open_file)
    open_file.close()


    