import discord
from collector import GoogleSheetCollector

#with open("token.txt", "r") as f:
    #lines = f.readlines()
    #token = lines[0]
    
#scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
#creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
#client = gspread.authorize(creds)
#sheet = client.open("F1").sheet1

data = GoogleSheetCollector()

Championship = data.CreateTeams()

print(Championship.ConstructorStandings())

#%%

#-------------
# =============================================================================
# 
# client = discord.Client()
# @client.event
# async def on_ready(): 
# 	print('We have logged in as {0.user}'.format(client))	
# 	await client.change_presence(activity=discord.Game(name=".help for commands")) 
# @client.event
# async def on_message(message):          
# 	if message.author == client.user:
# 		return    
# 	print(message.author.id,': Message from {0.author}: {0.content}'.format(message)) 
# 	if message.content.startswith(".constructstandings") and "div1" in message.content:
# 		await message.channel.send(league.constructorSortedList(0))
# 	if message.content.startswith(".constructstandings") and "div2" in message.content:
# 		await message.channel.send(league.constructorSortedList(1))
# 	if message.content.startswith(".stats"):
# 		msg = message.content.lower()
# 		splitmsg = msg.split()	
# 		oString = league.stats(str(splitmsg[1]))
# 		await message.channel.send(oString)
# 	if message.content.startswith(".drivstandings") and "div1" in message.content:
# 		await message.channel.send(league.driverSortedList(0))
# 	if message.content.startswith(".drivstandings") and "div2" in message.content:
# 		await message.channel.send(league.driverSortedList(1))
# 	if message.content.startswith(".help"):
# 		await message.channel.send(".constructstandings : sends the sorted list for constructors\n.stats : .stats [team name] shows the teams stats\n.drivstandings : sends the sorted list for the drivers")
# client.run(token)
# =============================================================================
