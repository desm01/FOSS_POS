class Customer:

    def __init__(self, name, address, postcode, date_of_birth, email_address, phone_number):
        self.name = name
        self.address = address
        self.postcode = postcode
        self.date_of_birth = date_of_birth
        self.email_address = email_address
        self.phone_number = phone_number

        self.points = 0
        self.purchases = []

    def change_name(self, new_name):
        self.name = new_name

    def change_address(self, new_address):
        self.address = new_address

    def change_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth
    
    def change_email_address(self, new_email_address):
        self.email_address = new_email_address
    
    def change_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def add_purchase(self, new_purchase):
        self.purchases.append(new_purchase)

    def add_points(self, points_to_be_added):
        self.points += points_to_be_added

    def remove_points(self, points_to_be_removed):
        self.points =- points_to_be_removed
        