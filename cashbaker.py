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

    if message.content.startswith('!cash'):
        with open("cbblinks.txt") as word_file:
            words = word_file.read().split()
        randtext = random.choice(words)

        await message.channel.send(randtext)


token = open("apitoken.txt")
client.run(token.readline())