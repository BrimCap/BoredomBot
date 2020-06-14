import discord
from discord.ext import commands
import asyncio

class countdown(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cd(self, ctx, amount : int):

        counting = True

        embed = discord.Embed(
            color = 0xadd8e6, 
            description = f'You have {amount} seconds left {ctx.author.mention}'
        )

        send = await ctx.send(embed = embed)

        while counting:

            amount -= 1

            embed = discord.Embed(
                color = 0xadd8e6, 
                description = f'You have {amount} seconds left {ctx.author.mention}'
            )

            await send.edit(embed = embed)

            if int(amount) == 0:
                await ctx.send(f'Your time is up {ctx.author.mention}')
                counting = False

            await asyncio.sleep(1)

    @cd.error
    async def cd_error_handler(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):   
                        
            if error.param.name == 'amount':
                await ctx.send("I wanna contdown but.. u didn't tell me for how long")
                

def setup(client):
    client.add_cog(countdown(client))