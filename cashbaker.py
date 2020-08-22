import discord
import random
from datetime import datetime, timedelta
import asyncio
import time
import sched
import notification

gamechoice = ""
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global gamechoice
    if message.author == client.user:
        if message.content.split() == ['Select', 'a', 'Game\u200e\u200e\u200e\xad\xad']:
            ow = '🔫'
            sot = '⛵'
            uno = '🃏'
            await message.add_reaction(ow)
            await message.add_reaction(sot)
            await message.add_reaction(uno)
        else:
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
    if message.content.startswith('!gamestart'):
        gamechoice = ""
        embed = discord.Embed(title="Game Lobby", description="An automated way to play")
        embed.add_field(name="Choosing a game", value=":black_joker: = Uno\n:sailboat: = Sea of Thieves\n:gun: = Overwatch")
        embed.add_field(name="Choosing a time", value="Type !gametime followed by a time in 24hr time (Example: '!gametime 17:00') alternatively, you can use 'now'.")
        await message.channel.send(content=None, embed=embed)
        await message.channel.send("Select a Game‎‎‎­­")
    if message.content.startswith('!gametime'):
        elapse = 0
        inv = message.author
        gtpps = message.content.split()
        gtps = str(gtpps[1])
        if gtps == "now":
            await message.channel.send(gamerole() + str(inv) + " would like to play " + gamechoice)
        elif gtps == "cancel":
            gamechoice = ""
            elapse = 0   
        else:
            gt = gtps.split(":")
            timen = datetime.now()
            a = timen.day
            b = timen.month
            c = timen.year
            givtime = datetime(c, b, a, int(gt[0]), int(gt[1]))
            timedif = givtime - timen
            strdif = str(timedif)
            splitdif = strdif.split(":")
            elapse = (int(splitdif[1])* 60 + int((splitdif[0] * 3600)))
            await message.channel.send("Time has been set.")
            notre = notification.notification(elapse)
            if notre == 1:
                await message.channel.send(gamerole() + str(inv) + " would like to play " + gamechoice)
        
@client.event
async def on_raw_reaction_add(RawReactionActionEvent):
    global gamechoice
    if RawReactionActionEvent.user_id == 744781938866257940:
        return
    else:
        remo = RawReactionActionEvent.emoji
        if remo.name == "🔫":
            gamechoice = "Overwatch"
            print(gamechoice)
        if remo.name == "⛵":
            gamechoice = "Sea of Thieves"
        if remo.name == "🃏":
            gamechoice = "Uno"

def randline(file):
    return random.choice(open(file).read().splitlines())

def gamerole():
    global gamechoice
    if gamechoice == "Sea of Thieves":
        a = "<@&744004992238616648>"
        return a
    if gamechoice == "Overwatch":
        a = "<@&716081848132042913>"
        return a
    if gamechoice == "Uno":
        a = "<@&738209588008058891>"
        return a
  
client.run(open("apitoken.txt").readline().strip())
