class constructor():

	def __init__(self, name, driverA, driverB):
		self.name = name
		self.driverA = driverA
		self.driverB = driverB

	def points(self):
		return self.driverA.points + self.driverB.points