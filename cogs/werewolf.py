import discord
from discord.ext import commands

class Werewolf(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['w'])
    async def werewolf(self, ctx):

        embed = discord.Embed(
            color = 0x22d4cb,
            title = "Werewolf",
            description = "Looks like we're having a game of werewolf today!\nIf you're interested in joining, react to this message."
        )

        embed.set_footer(text = "Minimum players: 4")

        message = await ctx.send(embed = embed)
        await message.add_reaction('😎')

        def check(message : discord.Message):
            return message.channel.id == ctx.channel.id and message.author.id == ctx.author.id

        try:
            wait = await self.client.wait_for('message', check = check, timeout = 60)
        except TimeoutError:
            await ctx.send("Welp looks like no one wants to join. Big sad")
            await message.delete()

        if wait.content.lower() == 'start':
            refetched = await message.channel.fetch_message(message.id)
            reaction = refetched.reactions

            players = []

            for user in reaction.users(after = self.client.user):
                players.append(user)

            self.play_game(ctx, players)


    async def play_game(self, ctx, players):

        await ctx.send(players)



def setup(client):
    client.add_cog(Werewolf(client))