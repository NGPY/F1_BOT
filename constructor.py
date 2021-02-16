class constructor():

	def __init__(self, name, driver1A, driver1B,driver2A,driver2B):
		self.name = name
		self.driver1A = driver1A
		self.driver1B = driver1B
		self.driver2A = driver2A
		self.driver2B = driver2B
		self.__updateteam__()

	def __updateteam__(self):
		if self.driver1A != None:
			self.driver1A.team = self
		if self.driver1B != None:
			self.driver1B.team = self
		if self.driver2B != None:
			self.driver2B = self
		if self.driver2A != None:
			self.driver2A = self
	def points(self,div):
		if div == 0:
			return int(self.driver1A.points) + int(self.driver1B.points)
		elif div == 1:
			return int(self.driver2A.points) + int(self.driver1B.points)

