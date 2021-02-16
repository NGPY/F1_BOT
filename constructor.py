class constructor():

	def __init__(self, name, driverA, driverB):
		self.name = name
		self.driverA = driverA
		self.driverB = driverB

	def points(self):
		return int(self.driverA.points) + int(self.driverB.points)