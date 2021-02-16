import discord
from drivers import driver
from constructor import constructor
from championship import championship
#Mercedes-----
mercDriverA = driver("Nod1","mercedes",49)
mercDriverB = driver("Niffle","mercedes",1)
mercTeam = constructor("mercedes",mercDriverA,mercDriverB)
#Alfa Romeo---
alfaDriverA = driver("ngpy","alfa romeo",23)
alfaDriverB = driver("alfie","alfa romeo",27)
alfaTeam = constructor("alfa romeo",alfaDriverA,alfaDriverB)
#Red Bull-----
bullDriverA = driver("Paradox","red Bull",14)
bullDriverB = driver("Vict","red Bull",17)
bullTeam = constructor("red Bull",bullDriverA,bullDriverB)
#McLaren------
mclaDriverA = driver("Emil","mclaren",14)
mclaDriverB = driver("GOOT","mclaren",12)
mclaTeam = constructor("mclaren",mclaDriverA,mclaDriverB)
#Aston Martin-
astoDriverA = driver("?","aston martin",0)
astoDriverB = driver("Lukanoid","aston martin",25)
astoTeam = constructor("aston martin",astoDriverA,astoDriverB)
#Alpine-------
alpiDriverA = driver("Wesley","alpine",2)
alpiDriverB = driver("Hintero","alpine",3)
alpiTeam = constructor("alpine",alpiDriverA,alpiDriverB)
#Ferrari------
ferrDriverA = driver("Sixyeu","ferrari",1)
ferrDriverB = driver("Luuk","ferrari",18)
ferrTeam = constructor("ferrari",ferrDriverA,ferrDriverB)
#Alpha Tauri--
alphDriverA = driver("Temperr","alpha tauri",23)
alphDriverB = driver("Immigration","alpha tauri",17)
alphTeam = constructor("alpha tauri",alphDriverA,alphDriverB)
#Haas---------
haasDriverA = driver("Maikki","haas",14)
haasDriverB = driver("Bean","haas",17)
haasTeam = constructor("haas",haasDriverA,haasDriverB)
#Williams-----
willDriverA = driver("Ghaz","williams",11)
willDriverB = driver("Mango","williams",12)
willTeam = constructor("williams",willDriverA,willDriverB)
#-------------
league = championship(
		alfaTeam,
		mercTeam,
		bullTeam,
		mclaTeam,
		astoTeam,
		alpiTeam,
		ferrTeam,
		alphTeam,
		haasTeam,
		willTeam
	)

client = discord.Client()
@client.event
async def on_ready(): 
	print('We have logged in as {0.user}'.format(client))	
	await client.change_presence(activity=discord.Game(name=".help for commands")) 
@client.event
async def on_message(message):          
	if message.author == client.user:
		return    
	print(message.author.id,': Message from {0.author}: {0.content}'.format(message)) 
	if message.content.startswith(".standings"):
		await message.channel.send(league.constructorSortedList())
	if message.content.startswith(".stats"):
		msg = message.content.lower()
		splitmsg = msg.split()	
		oString = league.stats(str(splitmsg[1]))

		await message.channel.send(oString)
	if message.content.startswith(".drivstandings"):
		await message.channel.send(league.driverSortedList())
client.run("token")