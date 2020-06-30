import discord
from discord.ext import commands

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):

        ping = discord.Embed(
            color = 0xffff00,
            description = f'⏳ | {round(self.client.latency * 1000)}ms'
        )

        await ctx.send(embed = ping)

def setup(client):
    client.add_cog(Ping(client))