from drivers import Driver

class Constructor():

    def __init__(self, name):

        # Name of constructor
        self.name = name

        # All drivers
        self.driver1a = None
        self.driver1b = None
        self.driver2a = None
        self.driver2b = None

        # Points
        self.Div1Points = 0
        self.Div2Points = 0
        self.points = 0

    def __UpdateTeam__(self):
        """
        Update each drivers team attribute
        Returns
        -------
        None.
        """

        if self.driver1a != None:
            self.driver1a.team = self
        if self.driver1b != None:
            self.driver1b.team = self
        if self.driver2a != None:
            self.driver2a.team = self
        if self.driver2b != None:
            self.driver2b.team = self
            

    def __UpdatePoints__(self):
        """
        Update points for Constructor. Does a running total so don't call twice. 
        Called at creation of object.
        Returns
        -------
        None.
        """

        if self.driver1a != None:
            self.Div1Points += self.driver1a.points
        if self.driver1b != None:
            self.Div1Points += self.driver1a.points
        if self.driver2a != None:
            self.Div2Points += self.driver2a.points
        if self.driver2b != None:
            self.Div2Points += self.driver2a.points
        self.points += self.Div1Points + self.Div2Points
        
    def TeamPointsString(self):
        return "Team: {} Points: {}\n".format(self.name, self.points) 
    
    def addDriver(self, name, points, div):
        
        driver = Driver(name, points, div)
               
        if driver.division == 1 and self.driver1a == None: self.driver1a = driver
        elif driver.division == 1 and self.driver1a != None: self.driver1b = driver
        
        if driver.division == 2 and self.driver2a == None: self.driver2a = driver
        elif driver.division == 2 and self.driver2a != None: self.driver2b = driver
        
        