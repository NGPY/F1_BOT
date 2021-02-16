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
	def constructorSortedList(self):
		oString = ""
		constructorStandings = [
				[self.con1.name,self.con1.points(),self.con1.driverA.name,self.con1.driverA.points,self.con1.driverB.name,self.con1.driverB.name],
				[self.con2.name,self.con2.points(),self.con2.driverA.name,self.con2.driverA.points,self.con2.driverB.name,self.con2.driverB.name],
				[self.con3.name,self.con3.points(),self.con3.driverA.name,self.con3.driverA.points,self.con3.driverB.name,self.con3.driverB.name],
				[self.con4.name,self.con4.points(),self.con4.driverA.name,self.con4.driverA.points,self.con4.driverB.name,self.con4.driverB.name],
				[self.con5.name,self.con5.points(),self.con5.driverA.name,self.con5.driverA.points,self.con5.driverB.name,self.con5.driverB.name],
				[self.con6.name,self.con6.points(),self.con6.driverA.name,self.con6.driverA.points,self.con6.driverB.name,self.con6.driverB.name],
				[self.con7.name,self.con7.points(),self.con7.driverA.name,self.con7.driverA.points,self.con7.driverB.name,self.con7.driverB.name],
				[self.con8.name,self.con8.points(),self.con8.driverA.name,self.con8.driverA.points,self.con8.driverB.name,self.con8.driverB.name],
				[self.con9.name,self.con9.points(),self.con9.driverA.name,self.con9.driverA.points,self.con9.driverB.name,self.con9.driverB.name],
				[self.con10.name,self.con10.points(),self.con10.driverA.name,self.con10.driverA.points,self.con10.driverB.name,self.con10.driverB.name],	
			] 
		con_standings_sorted = sorted(constructorStandings,key=lambda l:l[1], reverse=True) 
		for i in range(0,10):
			oString += "Team: " + con_standings_sorted[i][0] + " Points: " + str(con_standings_sorted[i][1])+" Driver 1: "+con_standings_sorted[i][2]+" Points: "+str(con_standings_sorted[i][3])+" Driver 2: "+con_standings_sorted[i][4]+" Points: "+str(con_standings_sorted[i][5])+"\n"
		return oString
	def driverSortedList(self):
		oString = ""
		driverStandings = [
		[self.con1.driverA.name,self.con1.driverA.points,],[self.con1.driverB.name,int(self.con1.driverB.points),],
		[self.con2.driverA.name,self.con2.driverA.points,],[self.con2.driverB.name,int(self.con2.driverB.points),],
		[self.con3.driverA.name,self.con3.driverA.points,],[self.con3.driverB.name,int(self.con3.driverB.points),],
		[self.con4.driverA.name,self.con4.driverA.points,],[self.con4.driverB.name,int(self.con4.driverB.points),],
		[self.con5.driverA.name,self.con5.driverA.points,],[self.con5.driverB.name,int(self.con5.driverB.points),],
		[self.con6.driverA.name,self.con6.driverA.points,],[self.con6.driverB.name,int(self.con6.driverB.points),],
		[self.con7.driverA.name,self.con7.driverA.points,],[self.con7.driverB.name,int(self.con7.driverB.points),],
		[self.con8.driverA.name,self.con8.driverA.points,],[self.con8.driverB.name,int(self.con8.driverB.points),],
		[self.con9.driverA.name,self.con9.driverA.points,],[self.con9.driverB.name,int(self.con9.driverB.points),],
		[self.con10.driverA.name,self.con10.driverA.points,],[self.con10.driverB.name,int(self.con10.driverB.points),],
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
		print(self.con1.name)
		oString = ""
		if self.name == str(fcon1[0]):
			oString = "Team: "+self.con1.name+" Points: "+str(self.con1.points())+"\n"
		elif self.name == self.con2.name:
			oString = "Team: "+self.con2.name+" Points: "+str(self.con2.points())+"\n"
		elif self.name == str(fcon3[0]):
			oString = "Team: "+self.con3.name+" Points: "+str(self.con3.points())+"\n"
		elif self.name == self.con4.name:
			oString = "Team: "+self.con4.name+" Points: "+str(self.con4.points())+"\n"
		elif self.name == str(fcon5[0]):
			oString = "Team: "+self.con5.name+" Points: "+str(self.con5.points())+"\n"
		elif self.name == self.con6.name:
			oString = "Team: "+self.con6.name+" Points: "+str(self.con6.points())+"\n"
		elif self.name == self.con7.name:
			oString = "Team: "+self.con7.name+" Points: "+str(self.con7.points())+"\n"
		elif self.name == str(fcon8[0]):
			oString = "Team: "+self.con8.name+" Points: "+str(self.con8.points())+"\n"
		elif self.name == self.con9.name:
			oString = "Team: "+self.con9.name+" Points: "+str(self.con9.points())+"\n"
		elif self.name == self.con10.name:
			oString = "Team: "+self.con10.name+" Points: "+str(self.con10.points())+"\n"
		return oString