import discord
import values1
import values2
import random
from values1 import driverstands1,constructorstands1,ball8
from values2 import driverstands2,constructorstands2

with open("token.txt", "r") as f:
    lines = f.readlines()
    token = lines[0]
client = discord.Client()
@client.event
async def on_ready(): 
	print('We have logged in as {0.user}'.format(client))	
	await client.change_presence(activity=discord.Game(name=".help for commands")) 
@client.event
async def on_message(message): # when a message is received
	print(message.author.id,': Message from {0.author}: {0.content}'.format(message))          # prints the message into the console
	if message.author == client.user:
		return            # if the message is the coming from the bot do not do any of the commands
	if message.content.startswith('.8ball'):    # simple 8 ball system
		num = random.randint(0,len(ball8))
		reply = ball8[num]
		await message.channel.send(reply)
	if message.content.startswith('.help'):   #if the message starts with .help messages that channel with the commands
		await message.channel.send('.8ball : 8ball response to anything\n.driverstands1 : shows div 1 driver standings\n.driverstands2 : shows div 2 driver standings\n.constructorstands1 : shows div 1 constructor standings\n.constructorstands2 : shows div 2 constructor standings\n.coin : coinflip\n.racetime : shows at what times races start')
	if message.content.startswith('.driverstands1'): # just sends a message with the sorted driver standings in pretty print
		await message.channel.send(driverstands1)
	if message.content.startswith('.constructorstands1'):  # just sends the constructor standings in pretty print
		await message.channel.send(constructorstands1)
	if message.content.startswith('.driverstands2'):
		await message.channel.send(driverstands2)
	if message.content.startswith('.constructorstands2'):
		await message.channel.send(constructorstands2)
	if message.content.startswith('.coin'):
		coin = random.randint(0,1)
		if coin == 0:
			await message.channel.send('Heads')
		elif coin == 1:
			await message.channel.send('Tails')
	if message.content.startswith('.join'):
		channel = message.author.voice.channel
		vc = await channel.connect()
		player = vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/Users/bened/OneDrive/Desktop/cock.mp3"))
		time.sleep(7)
		await vc.disconnect()

	if message.content.startswith('.racetime'):
		await message.channel.send('DIV 1:\nEvery Sunday 4pm **UTC**\nExceptions: NONE\nDIV 2:\nEvery Friday 7pm **UTC**\nExceptions: NONE')
	if message.content.startswith('.picofday'):
		await message.channel.send('https://cdn.discordapp.com/attachments/809005623899324419/809939640382521364/unknown.png')
client.run(token)