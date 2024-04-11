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

User1 = User("Sanjeevi", "Rajan")
User2 = User("Vel", "Prakash")

'''
print(User1.login_attributes)

User1.increment_login_attempts()
User1.increment_login_attempts()

print(User1.login_attributes)

User1.reset_login_attempts()

print(User1.login_attributes)
'''

class Privileges():
	def __init__(self):
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		print(self.privileges)

class Admin(User):

	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()

	

Admin1 = Admin("Sanjeevi", "Rajan1")
Admin1.privileges.show_privileges()
