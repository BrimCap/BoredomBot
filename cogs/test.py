import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def test(self, ctx, member : discord.Member = None):

        member = ctx.author if not member else member
        
        embed = discord.Embed(
            color = 0x0000FF,
            description = ''' Ok notice how i dont have a title.

            I just did ```py
            embed_name = discord.Embed(
                color = 0x0000FF,
                description = this.
            )
            ```

            And what we will be making today is the thing in the top.
            Look it says the name of the person i pinged but in a cool way.

            We will be making that today. (It's really easy btw)
            '''
        )

        embed.set_author(name = member.name, icon_url = member.avatar_url)

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Test(client))