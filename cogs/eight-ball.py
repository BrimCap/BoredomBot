import discord
import random
from discord.ext import commands

class EightBall(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.responses = [
            "As I see it, yes.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don’t count on it.",
            "It is certain.",
            "It is decidedly so.",
            "Most likely.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Outlook good.",
            "Reply hazy, try again.",
            "Signs point to yes.",
            "Very doubtful.",
            "Without a doubt.",
            "Yes.",
            "Yes – definitely.",
            "You may rely on it."
        ]

    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question):
        answer = discord.Embed(
            colour = 0x290fd1,
            description = random.choice(self.responses)
        )

        await ctx.send(embed = answer)

def setup(client):
    client.add_cog(EightBall(client))