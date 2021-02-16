import discord
from drivers import driver
from constructor import constructor
from championship import championship
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0]
scope = scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("F1").sheet1

#Mercedes-----
mercDriver1A = driver(sheet.cell(2,2).value,sheet.cell(2,1).value,sheet.cell(2,4).value,1)
mercDriver1B = driver(sheet.cell(3,2).value,sheet.cell(3,1).value,sheet.cell(3,4).value,1)
mercDriver2A = driver(sheet.cell(23,2).value,sheet.cell(23,1).value,sheet.cell(23,4).value,2)
mercDriver2B = driver(sheet.cell(24,2).value,sheet.cell(24,1).value,sheet.cell(24,4).value,2)
mercTeam = constructor("mercedes",mercDriver1A,mercDriver1B,mercDriver2A,mercDriver2B)
#Alfa Romeo---
alfaDriver1A = driver(sheet.cell(4,2).value,sheet.cell(4,1).value,sheet.cell(4,4).value,1)
alfaDriver1B = driver(sheet.cell(5,2).value,sheet.cell(5,1).value,sheet.cell(5,4).value,1)
alfaDriver2A = driver(sheet.cell(25,2).value,sheet.cell(25,1).value,sheet.cell(25,4).value,2)
alfaDriver2B = driver(sheet.cell(26,2).value,sheet.cell(26,1).value,sheet.cell(26,4).value,2)
alfaTeam = constructor("alfa romeo",alfaDriver1A,alfaDriver1B,alfaDriver2A,alfaDriver2B)
#Red Bull-----
bullDriver1A = driver(sheet.cell(6,2).value,sheet.cell(6,1).value,sheet.cell(6,4).value,1)
bullDriver1B = driver(sheet.cell(7,2).value,sheet.cell(7,1).value,sheet.cell(7,4).value,1)
bullDriver2A = driver(sheet.cell(27,2).value,sheet.cell(27,1).value,sheet.cell(27,4).value,2)
bullDriver2B = driver(sheet.cell(28,2).value,sheet.cell(28,1).value,sheet.cell(28,4).value,2)
bullTeam = constructor("red bull",bullDriver1A,bullDriver1B,bullDriver2A,bullDriver2B)
#McLaren------
time.sleep(60)
mclaDriver1A = driver(sheet.cell(8,2).value,sheet.cell(8,1).value,sheet.cell(8,4).value,1)
mclaDriver1B = driver(sheet.cell(9,2).value,sheet.cell(9,1).value,sheet.cell(9,4).value,1)
mclaDriver2A = driver(sheet.cell(29,2).value,sheet.cell(29,1).value,sheet.cell(29,4).value,2)
mclaDriver2B = driver(sheet.cell(30,2).value,sheet.cell(30,1).value,sheet.cell(30,4).value,2)
mclaTeam = constructor("mclaren",mclaDriver1A,mclaDriver1B,mclaDriver2A,mclaDriver2B)
#Aston Martin-
astoDriver1A = driver(sheet.cell(10,2).value,sheet.cell(10,1).value,sheet.cell(10,4).value,1)
astoDriver1B = driver(sheet.cell(11,2).value,sheet.cell(11,1).value,sheet.cell(11,4).value,1)
astoDriver2A = driver(sheet.cell(31,2).value,sheet.cell(31,1).value,sheet.cell(31,4).value,2)
astoDriver2B = driver(sheet.cell(32,2).value,sheet.cell(32,1).value,sheet.cell(32,4).value,2)
astoTeam = constructor("aston martin",astoDriver1A,astoDriver1B,astoDriver2A,astoDriver2B)
time.sleep(60)
#Alpine-------
alpiDriver1A = driver(sheet.cell(12,2).value,sheet.cell(12,1).value,sheet.cell(12,4).value,1)
alpiDriver1B = driver(sheet.cell(13,2).value,sheet.cell(13,1).value,sheet.cell(12,4).value,1)
alpiDriver2A = driver(sheet.cell(33,2).value,sheet.cell(33,1).value,sheet.cell(33,4).value,2)
alpiDriver2B = driver(sheet.cell(34,2).value,sheet.cell(34,1).value,sheet.cell(34,4).value,2)
alpiTeam = constructor("alpine",alpiDriver1A,alpiDriver1B,alpiDriver2A,alpiDriver2B)
#Ferrari------
ferrDriver1A = driver(sheet.cell(14,2).value,sheet.cell(14,1).value,sheet.cell(14,4).value,1)
ferrDriver1B = driver(sheet.cell(15,2).value,sheet.cell(15,1).value,sheet.cell(15,4).value,1)
ferrDriver2A = driver(sheet.cell(35,2).value,sheet.cell(35,1).value,sheet.cell(35,4).value,2)
ferrDriver2B = driver(sheet.cell(36,2).value,sheet.cell(36,1).value,sheet.cell(36,4).value,2)
ferrTeam = constructor("ferrari",ferrDriver1A,ferrDriver1B,ferrDriver2A,ferrDriver2B)
#Alpha Tauri--
time.sleep(60)
alphDriver1A = driver(sheet.cell(16,2).value,sheet.cell(16,1).value,sheet.cell(16,4).value,1)
alphDriver1B = driver(sheet.cell(17,2).value,sheet.cell(17,1).value,sheet.cell(17,4).value,1)
alphDriver2A = driver(sheet.cell(37,2).value,sheet.cell(37,1).value,sheet.cell(37,4).value,2)
alphDriver2B = driver(sheet.cell(38,2).value,sheet.cell(38,1).value,sheet.cell(38,4).value,2)
alphTeam = constructor("alpha tauri",alphDriver1A,alphDriver1B,alpiDriver2A,alpiDriver2B)
#Haas---------
haasDriver1A = driver(sheet.cell(18,2).value,sheet.cell(18,1).value,sheet.cell(18,4).value,1)
haasDriver1B = driver(sheet.cell(19,2).value,sheet.cell(19,1).value,sheet.cell(19,4).value,1)
haasDriver2A = driver(sheet.cell(39,2).value,sheet.cell(39,1).value,sheet.cell(39,4).value,2)
haasDriver2B = driver(sheet.cell(40,2).value,sheet.cell(40,1).value,sheet.cell(40,4).value,2)
haasTeam = constructor("haas",haasDriver1A,haasDriver1B,haasDriver2A,haasDriver2B)
#Williams-----
willDriver1A = driver(sheet.cell(20,2).value,sheet.cell(20,1).value,sheet.cell(20,4).value,1)
willDriver1B = driver(sheet.cell(21,2).value,sheet.cell(21,1).value,sheet.cell(21,4).value,1)
willDriver2A = driver(sheet.cell(41,2).value,sheet.cell(41,1).value,sheet.cell(41,4).value,2)
willDriver2B = driver(sheet.cell(42,2).value,sheet.cell(42,1).value,sheet.cell(42,4).value,2)
willTeam = constructor("williams",willDriver1A,willDriver1B,willDriver2A,willDriver2B)
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
	if message.content.startswith(".constructstandings") and "div1" in message.content:
		await message.channel.send(league.constructorSortedList(0))
	if message.content.startswith(".constructstandings") and "div2" in message.content:
		await message.channel.send(league.constructorSortedList(1))
	if message.content.startswith(".stats"):
		msg = message.content.lower()
		splitmsg = msg.split()	
		oString = league.stats(str(splitmsg[1]))
		await message.channel.send(oString)
	if message.content.startswith(".drivstandings") and "div1" in message.content:
		await message.channel.send(league.driverSortedList(0))
	if message.content.startswith(".drivstandings") and "div2" in message.content:
		await message.channel.send(league.driverSortedList(1))
	if message.content.startswith(".help"):
		await message.channel.send(".constructstandings : sends the sorted list for constructors\n.stats : .stats [team name] shows the teams stats\n.drivstandings : sends the sorted list for the drivers")
client.run(token)