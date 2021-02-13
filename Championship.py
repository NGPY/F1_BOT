class Championship():
    
    def __init__(self, Constructors):
        
        self.Constructors = Constructors
        
    def DriverStandings(self, division = 0):
        
        outputString = ""
        div1Standings = sorted([i.driver1a for i in self.Constructors] + [i.driver1b for i in self.Constructors], key=lambda l: l.points, reverse=True)
        div2Standings = sorted([i.driver2a for i in self.Constructors] + [i.driver2b for i in self.Constructors], key=lambda l: l.points, reverse=True)
        
        Standings = sorted(div1Standings + div2Standings, key=lambda l: l.points, reverse=True)
        
        if division == 1: # Div 1 or no input
            for con in div1Standings:
                if con != None: outputString += con.DriverPointsTeamString(True)
                
        if division == 2: # Div 2 or no input
            for con in div2Standings:
                if con != None: outputString += con.DriverPointsTeamString(True)
                
        if division == 0:
            for con in Standings:
                if con != None: outputString += con.DriverPointsTeamString()
                
        return outputString
    
    def ConstructorStandings(self, division = 0):
        
        outputString = ""
        div1Standings = sorted(self.Constructors, key=lambda l: l.Div1Points, reverse=True)
        div2Standings = sorted(self.Constructors, key=lambda l: l.Div2Points, reverse=True)
        
        if division == 1: # Div 1
            for con in div1Standings:
                outputString += con.TeamPointsString()
                
        elif division == 2: # Div 2 or no input
            for con in div2Standings:
                outputString += con.TeamPointsString()
                
        else:
            for con in self.Constructors:
                outputString += con.TeamPointsString()
                
        return outputString