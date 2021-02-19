class Driver():

    def __init__(self, name, points, division):

        self.name = name
        self.points = points
        self.division = division

    def DriverPointsTeamString(self, div = False):
        if div:
            return "Driver {} (Div {}) Points: {} Team: {}\n".format(self.name, self.division, self.points, self.team.name)
        else:
            return "Driver {} Points: {} Team: {}\n".format(self.name, self.points, self.team.name)
