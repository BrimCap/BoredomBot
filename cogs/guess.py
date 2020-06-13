import discord
import random
from discord.ext import commands

class guess(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def guess(self, ctx):

        pick = random.randint(1,10)
        await ctx.send(f'Pick a number between 1 and 10. {ctx.author.mention}')

        message = await self.client.wait_for('message', check = lambda message: message.author.id == ctx.author.id and message.channel.id == ctx.message.channel.id and message.guild.id == ctx.guild.id, timeout = 10.0)

        def number(message):
            if message.content == '1':
                return 1
            elif message.content == '2':
                return 2
            elif message.content == '3':
                return 3
            elif message.content == '4':
                return 4
            elif message.content == '5':
                return 5
            elif message.content == '6':
                return 6
            elif message.content == '7':
                return 7
            elif message.content == '8':
                return 8
            elif message.content == '9':
                return 9
            elif message.content == '10':
                return 10

        player = number(message)

        if pick == player:
            await ctx.send(f'<:tick:712964971079925790> You got it right! Now you have full bragging rights. {ctx.author.mention}')
        else:
            await ctx.send(f"<:wrong:712965175493394432> WA WAAA, thats wrong :( it's actually {pick}. {ctx.author.mention}") 

def setup(client):
    client.add_cog(guess(client))