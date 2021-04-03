from Objects.item import Item
import pickle



def store_items(list_of_items):
    file_name = "item_dump.pkl"

    open_file = open(file_name, "wb")
    pickle.dump(list_of_items, open_file)
    open_file.close()

    print("Storing Items")