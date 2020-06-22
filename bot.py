import discord 
import os
import tokener
from discord.ext import commands

TOKEN = tokener.get_token()

client = commands.Bot(command_prefix = '!b ')

@client.event
async def on_ready():
    print("")
    print("==========----------------✶----------------==========")
    print("")
    print("The bot is logged in!")
    print("Name: Reduce Boredom")
    print(f"Id: {client.user.id}")
    print(f"Prefix: !b ")
    print('')
    print(f"servers: {client.guilds}")
    print("")
    print("==========----------------✶----------------==========")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your commands"))

@client.command()
async def load(ctx, extenstion):
    client.load_extension(f"cogs.{extenstion}")

@client.command()
async def unload(ctx, extenstion):
    client.unload_extension(f"cogs.{extenstion}")

@client.event
async def on_message(message):

    if message.author.id == client.user.id:
        return
    
    if message.content.find("Im bored") != -1:
        await message.channel.send("Same")

    elif message.content.find("im bored") != -1:
        await message.channel.send("Same")

    await client.process_commands(message)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
