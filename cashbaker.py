import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower().split()
    for msgcon in msg:
        if msgcon == "fuck": 
            await message.delete()
            await message.channel.send("Watch your fucking whore mouth!")
    if message.content.startswith('!cash'):
        await message.channel.send(randline("rvi.txt") + " " + randline("cbblinks.txt"))
    if message.content.startswith('!speak'):
        await message.channel.send(randline("cbrp.txt"))
    if message.content.startswith('!help'):
        await message.channel.send("I am the Cash Baker Bot!\nYou can find my source code at https://github.com/ColbertN21/Cash-Baker-Bot \nCurrently my commands are as follows:\n!cash: Returns random tiktok link\n!speak: Returns random phrase\n!help: returns list of commands")
    
def randline(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)

client.run(open("apitoken.txt").readline().strip())
