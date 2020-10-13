class Restaurant:
    def __init__(self, name, cousine_type):
        """Description of my restaurant"""
        self.name = name
        self.cousine_type = cousine_type
        self.served = 0
        self.increment = 50

    def describe_restaurant(self):
        """information about restaurant"""
        print(f"Welcome to: {self.name} this is an {self.cousine_type}")

    def open_restaurant(self):
        """status"""
        print(f"Now: Open ")

    def number_served(self):
        """Number of people has been served"""
        print(f" {self.served} Is the number of people served ")

    def set_number_served(self):
        """People seleccion"""
        print(f"we have been set {self.served}  customer at this time")

    def increment_number_served(self, people):
        self.increment_number_served = self.increment + people
        print(f"In a business day we served: {self.increment} customers")



class IceCreamStand(Restaurant):
    def __init__(self, name, cousine_type):
        super().__init__(name, cousine_type)
        self.flavors = ['coco', 'mango', 'apple', 'peneaple', 'banana']

    def ice_cream_flavor(self):
        """All Ice cream flavors available"""
        print(f"Flavors availables: {self.flavors}")

new_rest = IceCreamStand('Ice cream', 'cariben cusine')
new_rest.ice_cream_flavor()





# food_restaurant = Restaurant('Ocean Club', 'Sea Food Cousine')
# food_restaurant.describe_restaurant()
# food_restaurant.open_restaurant()
# food_restaurant.number_served()
# food_restaurant.served = 20
# food_restaurant.number_served()
# food_restaurant.served = 10
# food_restaurant.set_number_served()
# food_restaurant.increment_number_served(20)
print('--------------------------------------------------------------------------------------------------------')



