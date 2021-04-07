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
    item5 = Item("Fanta", 1.29, 12, 1000008, "Drink", "Soft Drink")
    item6 = Item("Pizza", 8.99, 120, 100010, "Food", "Takeaway")
    item7 = Item("Burger", 9.99, 100, 1010, "Food", "Takeaway")
    item8 = Item("Chips", 2.99, 100, 10100, "Food", "Takeaway")
    item9 = Item("Gravy", 0.99, 120, 110, "Food", "Side")
    item10 = Item("Curry", 1.09, 10, 11110, "Food", "Side")
  
    itemList = []

    itemList.append(item1)
    itemList.append(item2)
    itemList.append(item3)
    itemList.append(item4)
    itemList.append(item5)
    itemList.append(item6)
    itemList.append(item7)
    itemList.append(item8)
    itemList.append(item9)
    itemList.append(item10)

    open_file = open(file_name, "wb")
    pickle.dump(itemList, open_file)
    open_file.close()

    print("Storing Items")
    