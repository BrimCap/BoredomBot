import discord
from discord.ext import commands

class Guilds(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def guilds(self, ctx):

        _guilds = [guild.name for guild in self.client.guilds]

        guild_embed = discord.Embed(
            color = 0x39bfbd,
            description = str(_guilds)
        )

        await ctx.author.send(embed = guild_embed)
        await ctx.send('Guilds send to DMs')

def setup(client):
    client.add_cog(Guilds(client))
