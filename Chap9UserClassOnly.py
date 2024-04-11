class User():

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attributes = 0

	def describe_user(self):
		print(self.first_name, self.last_name)

	def greet_user(self):
		print("Hello", self.first_name + "!")

	def increment_login_attempts(self):
		self.login_attributes += 1

	def reset_login_attempts(self):
		self.login_attributes = 0