from Objects.item import Item
import pickle



def store_items(list_of_items):
    file_name = "item_dump.pkl"

    open_file = open(file_name, "wb")
    pickle.dump(list_of_items, open_file)
    open_file.close()

    print("Storing Items")

def default_store_items():
    file_name = "item_dump.pkl"

    item1 = Item("Coke", 1.29, 24, 1000001, "Drink", "Soft Drink")
    item2 = Item("Sprite", 1.09, 30, 1000002, "Drink", "Soft Drink")
    item3 = Item("Red Bull", 1.59, 4, 1000003, "Drink", "Energy Drink")
    item4 = Item("Mars Bar", 0.79, 12, 100004, "Food", "Candy")

    itemList = []

    itemList.append(item1)
    itemList.append(item2)
    itemList.append(item3)
    itemList.append(item4)

    open_file = open(file_name, "wb")
    pickle.dump(itemList, open_file)
    open_file.close()

    print("Storing Items")
    