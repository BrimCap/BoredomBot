import discord
from discord.ext import commands

import asyncio

class Rps(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rps(self, ctx, target : discord.Member = None):

        
        
        start = discord.Embed(
            color = 0x00FFEC,
            title = f"{ctx.author.name} vs {target.name}",
            description = f"Both of you check your dms to start playing!"
        )

        # <!-- Functions -->

        async def pick(member : discord.Member):

            choices = [
                "rock",
                "paper",
                "scissors"
            ]

            def wait_for_choice(message: discord.Message):
                return message.author == member and not message.guild and message.content.lower() in choices

            await member.send("Choose `rock`, `paper` or `scissors`")

            choice = await self.client.wait_for('message', check = wait_for_choice)

            await member.send("Decision Made.")
            return choice.content.lower() 

        def win(targeted, author):
            if targeted == 'rock':

                if author == 'rock':
                    return 'Its a tie. ooo'

                elif author == 'paper':
                    return f'{ctx.author.mention} won!'

                elif author == 'scissors':
                    return f'{target.mention} won!'

            if targeted == 'paper':
                
                if author == 'rock':
                    return f'{target.mention} won!'

                elif author == 'paper':
                    return 'its a tie. ooo'

                elif author == 'scissors':
                    return f'{ctx.author.mention} won!'

            if targeted == 'scissors':
                
                if author == 'rock':
                    return f'{ctx.author.mention} won!'

                elif author == 'paper':
                    return f'{target.mention} won!'

                elif author == 'scissors':
                    return 'Its a tie. ooo'

        def confirmation(message : discord.Message):
            return message.author.id == target.id and message.channel.id == ctx.channel.id

        # <!-- -->

        if target:

            #ask for confirmation
            await ctx.send(f'{target.name}! {ctx.author.name} has challenged you to an RPS duel! say `yes` to continue and anything else cancel')

            try:
                confirm = await self.client.wait_for('message', check = confirmation, timeout = 60)

            except asyncio.TimeoutError:
                await ctx.send("He ran out of time :/")

            if confirm.content.lower() == 'yes':
                pass

            else:
                await ctx.send('Match cancelled')
                return


            #send the start message
            await ctx.send(embed = start)

            #send the message to both players
            await ctx.author.send("Opponent making a decision")
            player1 = await pick(target)
            player2 = await pick(ctx.author)

            picks = discord.Embed(
                color = 0x00FFEC,
                description = f'{target.mention} picked **{player1}** and **{player2}** was picked by {ctx.author.mention}'
            )

            winner = discord.Embed(
                colour = 0x00FFEC,
                description = win(player1, player2)
            )

            await ctx.send(embed = picks)
            await ctx.send(embed = winner)

def setup(client):
    client.add_cog(Rps(client))
