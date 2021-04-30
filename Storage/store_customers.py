from Storage.get_customers import get_customers
from Objects.customer import Customer
import pickle


def add_new_customer(new_customer):
    
    list_of_customers = []

    try:
        list_of_customers = get_customers()
        list_of_customers.append(new_customer)
    except:
        default_store_customers()
        add_new_customer(new_customer)

    file_name = "customer_dump.pkl"
    open_file = open(file_name, "wb")
    pickle.dump(list_of_customers, open_file)

    open_file.close()
    print("Storing customer")

def default_store_customers():
    file_name = "customer_dump.pkl"

    customer = Customer("Des", "27 Fake Street","BP04WQ" ,"1929/01/28", "des@email.com", "4356463")
    item_list = [customer]

    open_file = open(file_name, "wb")
    pickle.dump(item_list, open_file)
    open_file.close()
    print("Default Store")

