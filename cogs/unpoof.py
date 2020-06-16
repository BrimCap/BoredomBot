import discord
from discord.ext import commands

class unpoofer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unpoof(self, ctx, *, Name):

        bans = await ctx.guild.bans()

        for i in bans:
            if i.user.name.lower() == Name.lower():

                await ctx.guild.unban(i.user, reason = None)
                await ctx.send(f'👌 {i.user.name} unbanned!')

def setup(client):
    client.add_cog(unpoofer(client))