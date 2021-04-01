class Item:

    def __init__(self, name, price, quantity, pluNumber, itemType, category):
        self.name = name
        self.price = price
        self.quanitity = quantity
        self.pluNumber = pluNumber
        self.itemType = itemType
        self.category = category

    def change_name(self, new_name):
        self.name = new_name

    def change_price(self, new_price):
        self.price = new_price

    def change_pluNumber(self, new_number):
        self.pluNumber = new_number

    def change_itemType(self, new_itemType):
        self.itemType = new_itemType

    def change_category(self, new_category):
        self.category = new_category

    def print_details(self):
        print("Name: " + self.name)
        print("Price: " + str (self.price))
        print("Quantity: " + str (self.quanitity))
        print("PLU Number: " + str (self.pluNumber))
        print("Item Type: " + self.itemType)
        print("Category: " + self.category)

    def item_sold(self):
        if (self.quantity < 1):
            return ("Item Sold Out")
        else:
            self.quantity =- 1

    def increase_stock(self, number_to_add):
        if (number_to_add > 0):
            self.quantity += number_to_add

    def __del__(self):
        print("Destructor called, item deleted")
