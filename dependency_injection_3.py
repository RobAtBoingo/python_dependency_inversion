class A(object):
	def __init__(self, talking_thing):
		self.talking_thing = talking_thing

	def PrintIt(self):
		print(self.talking_thing.says())

class Y(object):
	def says(self):
		return "Y"

class Z(object):
	def says(self):
		return "Z"

if __name__ == "__main__":
	a = A(Y())
	a.PrintIt()