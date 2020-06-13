import discord
from discord.ext import commands

class test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def test(self, ctx):
        embed = discord.Embed(
            description = '<:BrickRed_Cool:702065730807660554>'
        )

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(test(client))