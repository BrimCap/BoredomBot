import discord
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def test(self, ctx):
        bans = await bans()

        await ctx.send(bans)

def setup(client):
    client.add_cog(test(client))