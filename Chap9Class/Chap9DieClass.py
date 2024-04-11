import random

class Die():

	def __init__(self, sides):
		self.sides = sides

	def roll_dice(self):
		print(random.randint(1, self.sides))

Die1 = Die(7)
Die1.roll_dice()
