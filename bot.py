import discord 
from discord.ext import commands

import os
import tokener

TOKEN = tokener.get_token()

client = commands.Bot(command_prefix = ['!b ', '!B '])

@client.event
async def on_ready():

    os.system('cls' if os.name == 'nt' else 'clear')

    print("")
    print("==========----------------✶----------------==========")
    print("")
    print("The bot is logged in!")
    print(f"Name: {client.user.name}")
    print(f"Id: {client.user.id}")
    print(f"Prefix: !b ")
    print('')
    print(f"Servers: {len(client.guilds)}")
    print("")
    print("==========----------------✶----------------==========")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your commands"))

@client.event
async def on_guild_join(guild):
    
    system_channel = guild.system_channel

    if system_channel:
        await system_channel.send('Server looks cool... imma vibe in here')

@client.command()
async def load(ctx, extenstion):
    client.load_extension(f"cogs.{extenstion}")

@client.command()
async def unload(ctx, extenstion):
    client.unload_extension(f"cogs.{extenstion}")

@client.event
async def on_message(message):

    boredom_messages = [
        "Im bored",
        "im bored",
        "I am bored",
        "i am bored",
        "I'm bored",
        "i'm bored"
    ]

    if message.author.id == client.user.id:
        return
    
    if message.content in boredom_messages:
        await message.channel.send("Same")

    await client.process_commands(message)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3].upper()}: Online')
        
client.run(TOKEN)
# :))
