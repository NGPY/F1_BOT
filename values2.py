mertotal2 = 0
bultotal2 = 0
mcltotal2 = 0
ractotal2 = 0
alptotal2 = 0
fertotal2 = 0
tautotal2 = 0
romtotal2 = 0
hastotal2 = 0
wiltotal2 = 0
standings2 = [
	["leonardo",0,"mer",0],
    ["?",0,"mer",0],
    ["screpper",0,"bul",0],
    ["lumpy",0,"bul",0],
    ["bruna",12,"mcl",4],
    ["ngpy",6,"mcl",7],
    ["luka",0,"rac",0],
    ["ghaz",26,"rac",1],
    ["wesley",2,"alp",9],
    ["websisson",0,"alp",0],
    ["water",8,"fer",6],
    ["para",1,"fer",10],
    ["eddie",18,"tau",2],
    ["bunaseara",4,"tau",8],
    ["hintero",0,"rom",0],
    ["stan",0,"rom",0],
    ["pedro",15,"has",3],
    ["niffle",0,"has",0],
    ["?",0,"wil",0],
    ["yann",10,"wil",5],
]

standingssort2 = sorted(standings2,key=lambda l:l[1], reverse=True)
driverstands2 = ""   # needed for += to work in for loop 
for i in range(0,20):
	a = str(standingssort2[i][0]) # setting the name of driver in standing sort
	b = str(standingssort2[i][1]) # setting the points
	c = str(standingssort2[i][2]) # setting the team
	abc = ("\nDriver: "+a+"  Points: "+b+"  Team: "+c+"") # adding all of these into one string
	driverstands2 += str(abc) # adding it into the final message used in the main events

for i in range(0,20):
	a = standings2[i][1]
	b = standings2[i][2]
	if b == "mer":
		mertotal2 += a
	elif b == "bul":
		bultotal2 += a
	elif b == "mcl":
		mcltotal2 += a	
	elif b == "rac":
		ractotal2 += a
	elif b == "alp":
		alptotal2 += a
	elif b == "fer":
		fertotal2 += a
	elif b == "tau":
		tautotal2 += a
	elif b == "rom":
		romtotal2 += a
	elif b == "has":
		hastotal2 += a
	elif b == "wil":
		wiltotal2 += a

constructor2 = [
	["Mercedes",mertotal2],     #standings for teams so i can sort them 
	["Red Bull",bultotal2],
	["McLaren",mcltotal2],
	["Racing Point",ractotal2],
	["Alpine",alptotal2],
	["Ferrari",fertotal2],
	["Alpha Tauri",tautotal2],  
	["Alfa Romeo",romtotal2],
	["Haas",hastotal2],
	["Williams",wiltotal2],
]
constructorssort2 = sorted(constructor2,key=lambda l:l[1], reverse=True) # sorts the teams in point order
constructorstands2 = ""

for i in range(0,10):                 
	a = str(constructorssort2[i][0])   # setting the name of in the sorted list
	b = str(constructorssort2[i][1])   # setting the points in the sorted list 
	ab = str("\nTeam: "+a+"  Points: "+b)    # adding points and name into string
	constructorstands2 += ab #addint it to the final message