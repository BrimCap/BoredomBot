import discord
from discord.ext import commands

import sys
import traceback

class Error(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        """
        The event triggered when an error is raised while invoking a command.

        Paramaters
        ----------

        ctx: commands.Context
            The context used for the command

        error: commands.CommandError
            The error raised
        """

        ignored = (commands.CommandNotFound, )

        error = (error, 'original', error)

        # Prevents the handler from handling commands that is handled locally
        if hasattr(ctx.command, 'on_error'):
            return

        # Prevents the handling errors that are ignored
        if isinstance(error, ignored):
            return

        # Prevents cogs with an overwritten cog_command_error being handled here
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send('This command has been disabled, so you cant use it. Big sad')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send("This cannot be used in DMs, try using it in a channel!")

            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send("Who dat? Whoever it is I couldn't find him.")

        else:
            print("Ignoring exception in command {}:".format(ctx.command), file = sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file = sys.stderr)



def setup(client):
    client.add_cog(Error(client))