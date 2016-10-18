class A(object):
	def PrintIt(self):
		z = Z()
		print(z.says())

class Z(object):
	def says(self):
		return "Z"

if __name__ == "__main__":
	a.PrintIt()
