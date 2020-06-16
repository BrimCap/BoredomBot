import discord
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def test(self, ctx):
        ban = await ctx.guild.bans()

        await ctx.send(ban)

def setup(client):
    client.add_cog(test(client))