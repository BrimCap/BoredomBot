import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command('help')



    @commands.command()
    async def help(self, ctx):


        print(self.client.cogs)

def setup(client):
    client.add_cog(Help(client))