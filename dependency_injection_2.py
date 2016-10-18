class A(object):
	def PrintIt(self):
		y = Y()
		print(y.says())

class Y(object):
	def says(self):
		return "Y"

class Z(object):
	def says(self):
		return "Z"
