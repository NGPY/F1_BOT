import discord
from drivers import driver
from constructor import constructor
from championship import championship
import gspread
from oauth2client.service_account import ServiceAccountCredentials
with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0]
scope = scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("F1").sheet1

#Mercedes-----
mercDriverA = driver(sheet.cell(2,2).value,sheet.cell(2,1).value,sheet.cell(2,4).value)
mercDriverB = driver(sheet.cell(3,2).value,sheet.cell(3,1).value,sheet.cell(3,4).value)
mercTeam = constructor("mercedes",mercDriverA,mercDriverB)
#Alfa Romeo---
alfaDriverA = driver(sheet.cell(4,2).value,sheet.cell(4,1).value,sheet.cell(4,4).value)
alfaDriverB = driver(sheet.cell(5,2).value,sheet.cell(5,1).value,sheet.cell(5,4).value)
alfaTeam = constructor("alfa romeo",alfaDriverA,alfaDriverB)
#Red Bull-----
bullDriverA = driver(sheet.cell(6,2).value,sheet.cell(6,1).value,sheet.cell(6,4).value)
bullDriverB = driver(sheet.cell(7,2).value,sheet.cell(7,1).value,sheet.cell(7,4).value)
bullTeam = constructor("red bull",bullDriverA,bullDriverB)
#McLaren------
mclaDriverA = driver(sheet.cell(8,2).value,sheet.cell(8,1).value,sheet.cell(8,4).value)
mclaDriverB = driver(sheet.cell(9,2).value,sheet.cell(9,1).value,sheet.cell(9,4).value)
mclaTeam = constructor("mclaren",mclaDriverA,mclaDriverB)
#Aston Martin-
astoDriverA = driver(sheet.cell(10,2).value,sheet.cell(10,1).value,sheet.cell(10,4).value)
astoDriverB = driver(sheet.cell(11,2).value,sheet.cell(11,1).value,sheet.cell(11,4).value)
astoTeam = constructor("aston martin",astoDriverA,astoDriverB)
#Alpine-------
alpiDriverA = driver(sheet.cell(12,2).value,sheet.cell(12,1).value,sheet.cell(12,4).value)
alpiDriverB = driver(sheet.cell(13,2).value,sheet.cell(13,1).value,sheet.cell(12,4).value)
alpiTeam = constructor("alpine",alpiDriverA,alpiDriverB)
#Ferrari------
ferrDriverA = driver(sheet.cell(14,2).value,sheet.cell(14,1).value,sheet.cell(14,4).value)
ferrDriverB = driver(sheet.cell(15,2).value,sheet.cell(15,1).value,sheet.cell(15,4).value)
ferrTeam = constructor("ferrari",ferrDriverA,ferrDriverB)
#Alpha Tauri--
alphDriverA = driver(sheet.cell(16,2).value,sheet.cell(16,1).value,sheet.cell(16,4).value)
alphDriverB = driver(sheet.cell(17,2).value,sheet.cell(17,1).value,sheet.cell(17,4).value)
alphTeam = constructor("alpha tauri",alphDriverA,alphDriverB)
#Haas---------
haasDriverA = driver(sheet.cell(18,2).value,sheet.cell(18,1).value,sheet.cell(18,4).value)
haasDriverB = driver(sheet.cell(19,2).value,sheet.cell(19,1).value,sheet.cell(19,4).value)
haasTeam = constructor("haas",haasDriverA,haasDriverB)
#Williams-----
willDriverA = driver(sheet.cell(20,2).value,sheet.cell(20,1).value,sheet.cell(20,4).value)
willDriverB = driver(sheet.cell(21,2).value,sheet.cell(21,1).value,sheet.cell(21,4).value)
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
	if message.content.startswith(".constructstandings"):
		await message.channel.send(league.constructorSortedList())
	if message.content.startswith(".stats"):
		msg = message.content.lower()
		splitmsg = msg.split()	
		oString = league.stats(str(splitmsg[1]))
		await message.channel.send(oString)
	if message.content.startswith(".drivstandings"):
		await message.channel.send(league.driverSortedList())
	if message.content.startswith(".help"):
		await message.channel.send(".constructstandings : sends the sorted list for constructors\n.stats : .stats [team name] shows the teams stats\n.drivstandings : sends the sorted list for the drivers")
client.run(token)