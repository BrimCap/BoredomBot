import discord
from discord.ext import commands

class poofer(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def poof(self, ctx, member : discord.Member, reason = None):

        if member.id == self.client.user.id:
            await ctx.send('Did you just poof me? smh')
        else:
            await ctx.send(f'You have been poofed {member.mention}')
            await member.kick(reason = reason)
            await member.send('You have been poofed sadly :(')

    @poof.error
    async def poof_error_handler(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'member':
                await ctx.send("U didn't ping anyone to poof. smh")

def setup(client):
    client.add_cog(poofer(client))