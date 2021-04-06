from Storage.store_records import record_transaction
from Objects.item import Item
import datetime

class Purchase:
    def __init__(self, list_of_items, served_by, customer):
        self.list_of_items = list_of_items
        self.total_cost = self.generate_cost()
        self.served_by = served_by
        self.customer = customer
        self.date_time = self.get_date_time()

        self.record_item()

    def get_date_time(self):
        return datetime.datetime.now()

    def details(self):
        label = ""
        for item in self.list_of_items:
            label += "Item : " + item.name + "\nPrice: £" + "{:.2f}".format(item.price) + "\n"
        label += "\nTotal Cost £" + "{:.2f}".format(self.total_cost)
        label += "\nServed By: " + self.served_by.name
        label += "\nDate Time: " + str(self.date_time.date())

        return label

    def generate_cost(self):
        cost = 0
        for item in self.list_of_items:
            cost += item.price
        return cost

    def record_item(self):
        record_transaction(self)