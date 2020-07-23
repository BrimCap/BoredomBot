import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def test_match(self, ctx, map):

        def remove_gamemode(full_map_name : str):

            underscore_split = full_map_name.split('_')

            game_mode_length = len(underscore_split[0])

            removal = game_mode_length + 1

            return full_map_name[removal:]

        await ctx.send(remove_gamemode(map))

def setup(client):
    client.add_cog(Test(client))