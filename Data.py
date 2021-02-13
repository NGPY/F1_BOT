from Driver import Driver
from Constructor import Constructor
from Championship import Championship

#%% DRIVERS ###################################################################

# Ferrari
FerrariDiv1DriverA = Driver("Sixyeu", 0, 1)
FerrariDiv1DriverB = Driver("Luuk0161", 0, 1)
FerrariDiv2DriverA = Driver("Water", 0, 2)
FerrariDiv2DriverB = Driver("Para", 0, 2)

# Mercedes
MercedesDiv1DriverA = Driver("Nod1Man", 0, 1)
MercedesDiv1DriverB = Driver("Niffle", 0, 1)
MercedesDiv2DriverA = Driver("Leonardo1", 0, 2)
MercedesDiv2DriverB = Driver("SaudagarUntaLeherPendek", 0, 2)


#%% CONSTRUCTORS ###################################################################

Ferrari = Constructor("Ferrari", FerrariDiv1DriverA, FerrariDiv1DriverB, FerrariDiv2DriverA, FerrariDiv2DriverB)
Mercedes = Constructor("Mercedes", MercedesDiv1DriverA, MercedesDiv1DriverB, MercedesDiv2DriverA, MercedesDiv2DriverB)

AllTeams = [Ferrari, Mercedes]

#%% CHAMPIONSHIP ###################################################################

Championship = Championship(AllTeams)

if __name__ == "__main__":
    
    print("Testing...")
    
    print("Constructor points both divisions")
    print(Championship.ConstructorStandings())
    
    print("Constructor points div 1")
    print(Championship.ConstructorStandings(1))
    
    print("Constructor points div 2")
    print(Championship.ConstructorStandings(2))
    
    print("Driver standings both divisions")
    print(Championship.DriverStandings())
    
    print("Driver standings div 1")
    print(Championship.DriverStandings(1))
    
    print("Driver standings div 2")
    print(Championship.DriverStandings(2))