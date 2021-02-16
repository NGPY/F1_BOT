class championship():

	def __init__(self, 
			con1, 
			con2,
			con3,
			con4,
			con5,
			con6,
			con7,
			con8,
			con9,
			con10,
			):
		self.con1 = con1
		self.con2 = con2
		self.con3 = con3
		self.con4 = con4
		self.con5 = con5
		self.con6 = con6
		self.con7 = con7
		self.con8 = con8
		self.con9 = con9
		self.con10 = con10
	def constructorSortedList(self,div):
		if div == 0:
			oString = ""
			constructorStandings = [
				[self.con1.name,self.con1.points(0),self.con1.driver1A.name,self.con1.driver1A.points,self.con1.driver1B.name,self.con1.driver1B.points],
				[self.con2.name,self.con2.points(0),self.con2.driver1A.name,self.con2.driver1A.points,self.con2.driver1B.name,self.con2.driver1B.points],
				[self.con3.name,self.con3.points(0),self.con3.driver1A.name,self.con3.driver1A.points,self.con3.driver1B.name,self.con3.driver1B.points],
				[self.con4.name,self.con4.points(0),self.con4.driver1A.name,self.con4.driver1A.points,self.con4.driver1B.name,self.con4.driver1B.points],
				[self.con5.name,self.con5.points(0),self.con5.driver1A.name,self.con5.driver1A.points,self.con5.driver1B.name,self.con5.driver1B.points],
				[self.con6.name,self.con6.points(0),self.con6.driver1A.name,self.con6.driver1A.points,self.con6.driver1B.name,self.con6.driver1B.points],
				[self.con7.name,self.con7.points(0),self.con7.driver1A.name,self.con7.driver1A.points,self.con7.driver1B.name,self.con7.driver1B.points],
				[self.con8.name,self.con8.points(0),self.con8.driver1A.name,self.con8.driver1A.points,self.con8.driver1B.name,self.con8.driver1B.points],
				[self.con9.name,self.con9.points(0),self.con9.driver1A.name,self.con9.driver1A.points,self.con9.driver1B.name,self.con9.driver1B.points],
				[self.con10.name,self.con10.points(0),self.con10.driver1A.name,self.con10.driver1A.points,self.con10.driver1B.name,self.con10.driver1B.points],	
				] 
			con_standings_sorted = sorted(constructorStandings,key=lambda l:l[1], reverse=True) 
			for i in range(0,10):
				oString += "Team: " + con_standings_sorted[i][0] + " Points: " + str(con_standings_sorted[i][1])+" Driver 1: "+con_standings_sorted[i][2]+" Points: "+str(con_standings_sorted[i][3])+" Driver 2: "+con_standings_sorted[i][4]+" Points: "+str(con_standings_sorted[i][5])+"\n"
			return oString
		elif div == 1:
			oString = ""
			constructorStandings = [
				[self.con1.name,self.con1.points(1),self.con1.driver2A.name,self.con1.driver2A.points,self.con1.driver2B.name,self.con1.driver2B.points],
				[self.con2.name,self.con2.points(1),self.con2.driver2A.name,self.con2.driver2A.points,self.con2.driver2B.name,self.con2.driver2B.points],
				[self.con3.name,self.con3.points(1),self.con3.driver2A.name,self.con3.driver2A.points,self.con3.driver2B.name,self.con3.driver2B.points],
				[self.con4.name,self.con4.points(1),self.con4.driver2A.name,self.con4.driver2A.points,self.con4.driver2B.name,self.con4.driver2B.points],
				[self.con5.name,self.con5.points(1),self.con5.driver2A.name,self.con5.driver2A.points,self.con5.driver2B.name,self.con5.driver2B.points],
				[self.con6.name,self.con6.points(1),self.con6.driver2A.name,self.con6.driver2A.points,self.con6.driver2B.name,self.con6.driver2B.points],
				[self.con7.name,self.con7.points(1),self.con7.driver2A.name,self.con7.driver2A.points,self.con7.driver2B.name,self.con7.driver2B.points],
				[self.con8.name,self.con8.points(1),self.con8.driver2A.name,self.con8.driver2A.points,self.con8.driver2B.name,self.con8.driver2B.points],
				[self.con9.name,self.con9.points(1),self.con9.driver2A.name,self.con9.driver2A.points,self.con9.driver2B.name,self.con9.driver2B.points],
				[self.con10.name,self.con10.points(1),self.con10.driver2A.name,self.con10.driver2A.points,self.con10.driver2B.name,self.con10.driver2B.points],	
				] 
			con_standings_sorted = sorted(constructorStandings,key=lambda l:l[1], reverse=True) 
			for i in range(0,10):
				oString += "Team: " + con_standings_sorted[i][0] + " Points: " + str(con_standings_sorted[i][1])+" Driver 1: "+con_standings_sorted[i][2]+" Points: "+str(con_standings_sorted[i][3])+" Driver 2: "+con_standings_sorted[i][4]+" Points: "+str(con_standings_sorted[i][5])+"\n"
			return oString
	def driverSortedList(self,div):
		if div == 0:
			oString = ""
			driverStandings = [
			[self.con1.driver1A.name,int(self.con1.driver1A.points,)],[self.con1.driver1B.name,int(self.con1.driver1B.points,)],
			[self.con2.driver1A.name,int(self.con2.driver1A.points,)],[self.con2.driver1B.name,int(self.con2.driver1B.points,)],
			[self.con3.driver1A.name,int(self.con3.driver1A.points,)],[self.con3.driver1B.name,int(self.con3.driver1B.points,)],
			[self.con4.driver1A.name,int(self.con4.driver1A.points,)],[self.con4.driver1B.name,int(self.con4.driver1B.points,)],
			[self.con5.driver1A.name,int(self.con5.driver1A.points,)],[self.con5.driver1B.name,int(self.con5.driver1B.points,)],
			[self.con6.driver1A.name,int(self.con6.driver1A.points,)],[self.con6.driver1B.name,int(self.con6.driver1B.points,)],
			[self.con7.driver1A.name,int(self.con7.driver1A.points,)],[self.con7.driver1B.name,int(self.con7.driver1B.points,)],
			[self.con8.driver1A.name,int(self.con8.driver1A.points,)],[self.con8.driver1B.name,int(self.con8.driver1B.points,)],
			[self.con9.driver1A.name,int(self.con9.driver1A.points,)],[self.con9.driver1B.name,int(self.con9.driver1B.points,)],
			[self.con10.driver1A.name,int(self.con10.driver1A.points,)],[self.con10.driver1B.name,int(self.con10.driver1B.points,)],
			]
			driv_standings_sorted = sorted(driverStandings,key=lambda l:l[1], reverse=True) 
			for i in range(0,20):
				oString += "Driver: "+driv_standings_sorted[i][0]+" Points: "+str(driv_standings_sorted[i][1])+"\n"
			return oString
		if div == 1:
			oString = ""
			driverStandings = [
			[self.con1.driver2A.name,int(self.con1.driver2A.points,)],[self.con1.driver2B.name,int(self.con1.driver2B.points,)],
			[self.con2.driver2A.name,int(self.con2.driver2A.points,)],[self.con2.driver2B.name,int(self.con2.driver2B.points,)],
			[self.con3.driver2A.name,int(self.con3.driver2A.points,)],[self.con3.driver2B.name,int(self.con3.driver2B.points,)],
			[self.con4.driver2A.name,int(self.con4.driver2A.points,)],[self.con4.driver2B.name,int(self.con4.driver2B.points,)],
			[self.con5.driver2A.name,int(self.con5.driver2A.points,)],[self.con5.driver2B.name,int(self.con5.driver2B.points,)],
			[self.con6.driver2A.name,int(self.con6.driver2A.points,)],[self.con6.driver2B.name,int(self.con6.driver2B.points,)],
			[self.con7.driver2A.name,int(self.con7.driver2A.points,)],[self.con7.driver2B.name,int(self.con7.driver2B.points,)],
			[self.con8.driver2A.name,int(self.con8.driver2A.points,)],[self.con8.driver2B.name,int(self.con8.driver2B.points,)],
			[self.con9.driver2A.name,int(self.con9.driver2A.points,)],[self.con9.driver2B.name,int(self.con9.driver2B.points,)],
			[self.con10.driver2A.name,int(self.con10.driver2A.points,)],[self.con10.driver2B.name,int(self.con10.driver2B.points,)],
			]
			driv_standings_sorted = sorted(driverStandings,key=lambda l:l[1], reverse=True) 
			for i in range(0,20):
				oString += "Driver: "+driv_standings_sorted[i][0]+" Points: "+str(driv_standings_sorted[i][1])+"\n"
			return oString
	def stats(self,name):
		self.name = name
		fcon1 = self.con1.name.split()
		fcon3 = self.con3.name.split()
		fcon5 = self.con5.name.split()
		fcon8 = self.con8.name.split()
		oString = ""
		if self.name == str(fcon1[0]):
			oString = "Team: "+self.con1.name+" Points: "+str(self.con1.points(0))+"\n"
		elif self.name == self.con2.name:
			oString = "Team: "+self.con2.name+" Points: "+str(self.con2.points(0))+"\n"
		elif self.name == str(fcon3[0]):
			oString = "Team: "+self.con3.name+" Points: "+str(self.con3.points(0))+"\n"
		elif self.name == self.con4.name:
			oString = "Team: "+self.con4.name+" Points: "+str(self.con4.points(0))+"\n"
		elif self.name == str(fcon5[0]):
			oString = "Team: "+self.con5.name+" Points: "+str(self.con5.points(0))+"\n"
		elif self.name == self.con6.name:
			oString = "Team: "+self.con6.name+" Points: "+str(self.con6.points(0))+"\n"
		elif self.name == self.con7.name:
			oString = "Team: "+self.con7.name+" Points: "+str(self.con7.points(0))+"\n"
		elif self.name == str(fcon8[0]):
			oString = "Team: "+self.con8.name+" Points: "+str(self.con8.points(0))+"\n"
		elif self.name == self.con9.name:
			oString = "Team: "+self.con9.name+" Points: "+str(self.con9.points(0))+"\n"
		elif self.name == self.con10.name:
			oString = "Team: "+self.con10.name+" Points: "+str(self.con10.points(0))+"\n"
		return oString