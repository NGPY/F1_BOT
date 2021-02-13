total = 0               
mertotal1 = 0
bultotal1 = 0
mcltotal1 = 0
ractotal1 = 0
alptotal1 = 0
fertotal1 = 0
tautotal1 = 0
romtotal1 = 0
hastotal1 = 0
wiltotal1 = 0

ball8 = ["It is certain","It is decidedly so.","Without a doubt","Yes - definitely.","You may rely on it.","As I see it, yes.","Most likely.","Outlook good.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Beetter not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it","My sources say no.","Outlook not so good.","Very doubtful."]

standings1 = [                 
	["nod1",0,"mer"],
	["niffle",2,"mer"],
	["paradox",10,"bul"],
	["uhlicek",0,"bul"],
	["emil",0,"mcl"],
	["goot",4,"mcl"],
	["eliax",0,"rac"],
	["jmlima44",0,"rac"],
	["majortom",0,"alp"],
	["hintero",25,"alp"],
	["fredrik",0,"fer"],
	["luuk",0,"fer"],
	["temperr",1,"tau"],
	["immigration",0,"tau"],
	["alfie",12,"rom"],
	["ngpy",8,"rom"],
	["maikki",18,"has"],
	["bean",15,"has"],
	["dawid",6,"wil"],
	["mango",0,"wil"],
]
standingssort1 = sorted(standings1,key=lambda l:l[1], reverse=True)
driverstands1 = ""   # needed for += to work in for loop 
for i in range(0,20):
	a = str(standingssort1[i][0]) # setting the name of driver in standing sort
	b = str(standingssort1[i][1]) # setting the points
	c = str(standingssort1[i][2]) # setting the team
	abc = ("\nDriver: "+a+"  Points: "+b+"  Team: "+c+"") # adding all of these into one string
	driverstands1 += str(abc) # adding it into the final message used in the main events

for i in range(0,20):
	a = standings1[i][1]
	b = standings1[i][2]
	if b == "mer":
		mertotal1 += a
	elif b == "bul":
		bultotal1 += a
	elif b == "mcl":
		mcltotal1 += a	
	elif b == "rac":
		ractotal1 += a
	elif b == "alp":
		alptotal1 += a
	elif b == "fer":
		fertotal1 += a
	elif b == "tau":
		tautotal1 += a
	elif b == "rom":
		romtotal1 += a
	elif b == "has":
		hastotal1 += a
	elif b == "wil":
		wiltotal1 += a 

constructor1 = [
	["Mercedes",mertotal1],     
	["Red Bull",bultotal1],
	["McLaren",mcltotal1],
	["Racing Point",ractotal1],
	["Alpine",alptotal1],
	["Ferrari",fertotal1],
	["Alpha Tauri",tautotal1],
	["Alfa Romeo",romtotal1],
	["Haas",hastotal1],
	["Williams",wiltotal1],
]

constructorssort1 = sorted(constructor1,key=lambda l:l[1], reverse=True)
constructorstands1 = ""   # needed for += in for loop

for i in range(0,10):                 
	a = str(constructorssort1[i][0])   # setting the name of in the sorted list
	b = str(constructorssort1[i][1])   # setting the points in the sorted list 
	ab = str("\nTeam: "+a+"  Points: "+b)    # adding points and name into string
	constructorstands1 += ab #addint it to the final message