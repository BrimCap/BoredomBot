import discord
import asyncio
import random
from discord.ext import commands
from asyncio import TimeoutError

class rps(commands.Cog):

    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def rps(self, ctx, member : discord.Member = None):

        if member:

            await ctx.send(f'{member.mention}! {ctx.author.mention} has challenged you to an **RPS** duel! Reply with `yes` or `no`')

            def confirm(message : discord.Message):
                return message.author.id == member.id and message.content.lower() and message.channel.id == ctx.channel.id

            try:
                confirmation = await self.client.wait_for('message', check = confirm, timeout = 20)
            except TimeoutError:
                await ctx.send(f'{member.mention} took too long so the match has been cancelled')

            if confirmation.content.lower() == 'yes':
                pass
            else:
                await ctx.send(f'{member.mention} has declined the challenge')
                return


            starting = discord.Embed(
                colour = 0xadd8e6,
                title = f'The Game Is Starting!',
                description = f'{member.mention} and {ctx.author.mention} check your dms!' 
            )

            await ctx.send(embed = starting)

            await ctx.author.send('Opponent making a decision...')
            await member.send('Choose `rock`, `paper` or `scissors`')

            def player1(message : discord.Message) -> bool:
                accepted = ['rock', 'r', 'paper', 'p', 'scissors', 's']
                return message.author.id == member.id and not message.guild and message.content.lower() in accepted

            try:
                rps1 = await self.client.wait_for('message', check = player1, timeout = 120)
            except TimeoutError:
                return await ctx.send('You took too long.. :/')

            await member.send('Decision Made.')
            
            if rps1.content.lower() in ['rock', 'r']:
                pick = rps1.content.lower()
            elif rps1.content.lower() in ['paper', 'p']:
                pick = rps1.content.lower()
            elif rps1.content.lower() in ['scissors', 's']:
                pick = rps1.content.lower() 

            await ctx.author.send('Pick `rock`, `paper` or `scissors`')

            def player2(message: discord.Message) -> bool:
                accepted = ['rock', 'r', 'paper', 'p', 'scissors', 's']
                return message.author.id == ctx.author.id and not message.guild and message.content.lower() in accepted

            try:
                rps2 = await self.client.wait_for('message', check = player2, timeout = 120) 
            except TimeoutError:
                ctx.send('You took too long :/')  

            await ctx.author.send('Decision Made.') 

            if rps2.content.lower() in ['rock', 'r']:
                choice = rps2.content.lower()

            elif rps2.content.lower() in ['paper', 'p']:
                choice = rps2.content.lower()

            elif rps2.content.lower() in ['scissors', 's']:
                choice = rps2.content.lower()
                


            embed = discord.Embed(
                colour = 0xadd8e6,
                description = f'{ctx.author.mention} picked **{choice.lower()}** and **{pick.lower()}** was picked by {member.mention}' 
            )

            await ctx.send(embed = embed)

            def win(choice, pick):
                    
                if pick == 'rock':
                    if choice == 'rock':
                        return "It's a draw!"
                    elif choice == 'paper':
                        return f'{ctx.author.mention} won!'
                    elif choice == 'scissors':
                        return f'{member.mention} won!'

                elif pick == 'paper':
                    if choice == 'rock':
                        return f"{member.mention} won!"
                    elif choice == 'paper':
                        return "it's a draw!"
                    elif choice == 'scissors':
                        return f'{ctx.author.mention} won!'

                elif pick == 'scissors':
                    if choice == 'rock':
                        return f"{ctx.author.mention} won!"
                    elif choice == 'paper':
                        return f'{member.mention} won!'
                    elif choice == 'scissors':
                        return "It's a draw!"

            winner = discord.Embed(
                colour = 0xadd8e6,
                description = win(choice, pick)
            )

            await ctx.send(embed = winner)

        else:

            accepted = ['rock', 'paper', 'scissors']

            com_choice = random.choice(accepted)

            await ctx.send('Pick `rock`, `paper` or `scissors`')

            def player(message : discord.Message):
                return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id and message.guild == ctx.guild and message.content.lower() in accepted 

            send = await self.client.wait_for('message', check = player)

            await ctx.send(f'You chose **{send.content}**, I chose **{com_choice}**')
            await ctx.send('Who won? idk')

def setup(client):
    client.add_cog(rps(client))