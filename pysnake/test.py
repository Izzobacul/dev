class Test:
	def __init__(self, x: str):
		self.x = x
	def __float__(self):
		return(float(int(self.x)))

t = Test("647")

print(float(t))