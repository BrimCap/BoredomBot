import discord
from discord.ext import commands

class Poof(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command(aliases = ['kick'])
    async def poof(self, ctx, member : discord.Member, *, reason = None):

        async def too_powerful():
            await ctx.send(f"I'm sorry my master, but {member.mention} is too powerful.")
            

        if member.id == self.client.user.id:
            await ctx.send('Did you just poof me? smh')

        elif member.id == ctx.guild.owner_id:
            await too_powerful()
            return

        elif ctx.me.top_role < member.top_role:
            await too_powerful()
            return
            
        else:

            try:
                await member.send(f'You have been poofed sadly. \nReason: ```{reason}```')
                await member.kick(reason = reason)

            except discord.Forbidden:
                await too_powerful()
            else:
                await ctx.send(f':ok_hand: Just poofed {member.mention}')

    @poof.error
    async def poof_error_handler(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                await ctx.send("U didn't ping anyone to poof. smh")

        else:
            raise error

def setup(client):
    client.add_cog(Poof(client))
