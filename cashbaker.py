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
    msg = message.content.split()
    for msgcon in msg:
        if msgcon == "fuck":
            await message.delete()
            await message.channel.send("Watch your fucking whore mouth!")
    if message.content.startswith('!cash'):
        randlink = randline("cbblinks.txt")
        randi = randline("rvi.txt")
        await message.channel.send(randi + " " + randlink)
    if message.content.startswith('!speak'):
        randphrase = randline("cbrp.txt")
        await message.channel.send(randphrase)
    if message.content.startswith('!help'):
        await message.channel.send("I am the Cash Baker Bot!\nYou can find my source code at https://github.com/ColbertN21/Cash-Baker-Bot \nCurrently my commands are as follows:\n!cash: Returns random tiktok link\n!speak: Returns random phrase\n!help: returns list of commands")
    
def randline(file):
    lines = open(file).read().splitlines()
    return random.choice(lines)

token = open("apitoken.txt")
client.run(token.readline())
