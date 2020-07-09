import discord
from discord.ext import commands

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

        # <!-- -->

        if target:

            #send the start message
            await ctx.send(embed = start)

            #send the message to both players
            await ctx.author.send("Opponent making a decision")
            player1 = await pick(target)
            player2 = await pick(ctx.author)

            who_won = discord.Embed(
                color = 0x00FFEC,
                description = f'''{target.mention} picked **{player1}** and **{player2}** was picked by {ctx.author.mention}

                **{win(player1, player2)}**'''
            )

            await ctx.send(embed = who_won)

            


def setup(client):
    client.add_cog(Rps(client))
