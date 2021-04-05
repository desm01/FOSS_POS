from Objects.item import Item
import pickle

def record_transaction(transaction):

    try:
        list_of_transactions = get_transactions()
    except:
        list_of_transactions = []
        

    file_name = "records_dump.pkl"
    open_file = open(file_name, "wb")
    
    list_of_transactions.append(transaction)
    pickle.dump(list_of_transactions, open_file)
    open_file.close()

    print(transaction.list_of_items)
    print(transaction.total_cost)
    print(transaction.served_by)
    print(transaction.customer)
    print("Recording")

def get_transactions():
    file_name = "records_dump.pkl"
    open_file = open(file_name, "rb")
    loaded_list = pickle.load(open_file)
    open_file.close()
    return loaded_list
