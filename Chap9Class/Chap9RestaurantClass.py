class Restaurant():

	def __init__(self, cuisine_type, restaurant_name):
		self.cuisine_type = cuisine_type
		self.restaurant_name = restaurant_name
		self.number_served = 0

	def describe_restaurant(self):
		print("restaurant_name", self.restaurant_name)
		print("cuisine_type", self.cuisine_type)

	def open_restaurant(self):
		print("The Restaurant is Open!")

	def increment_number_served(self):
		self.number_served += 1

	def set_number_served(self, served):
		self.number_served = served
		print(self.number_served)

jeevi = Restaurant("Japanese", "Jeevan's")

'''
print(jeevi.restaurant_name)
print(jeevi.cuisine_type)

jeevi.describe_restaurant()
jeevi.open_restaurant()

print()

print(jeevi.number_served)
jeevi.increment_number_served()
jeevi.increment_number_served()
print(jeevi.number_served)

jeevi.set_number_served(500)
'''

class IceCreamStand(Restaurant):

	def __init__(self, cuisine_type, restaurant_name):
		super().__init__(cuisine_type, restaurant_name)
		self.flavors = ["Banana", "Vanilla"]

	def show_flavors(self):
		print(self.flavors)
		
'''
jeevans = IceCreamStand("American", "Vel's")
jeevans.show_flavors()
'''