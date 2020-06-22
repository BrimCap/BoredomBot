import discord
import requests 
import bs4
from discord.ext import commands

class _corona(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def corona(self, ctx, country = None):

        await ctx.channel.trigger_typing()
        if country == None:
            res = requests.get('https://www.worldometers.info/coronavirus/')
            title = 'WORLD'
        else:
            res = requests.get('https://www.worldometers.info/coronavirus/country/' + str(country))
            title = country.upper()

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        numbers = soup.select('.maincounter-number span')
        cc = numbers[0].text
        deaths = numbers[1].text
        recoverd = numbers[2].text

        embed = discord.Embed(
            colour = 0xFF0000,
            description = "Here are some info i managed to find while scraping :/",
            title = title
        )

        embed.add_field(name="Confirmed Cases", value=f"{cc}", inline=False)
        embed.add_field(name="Recoverd", value=f"{recoverd}", inline=False)
        embed.add_field(name="Deaths", value=f"{deaths}", inline=False)
        embed.set_footer(text = f"Requested by | {ctx.author}")
        embed.set_author(name = 'CORONAVIRUS', icon_url = 'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/1800x1200_virus_3d_render_red_03_other.jpg?resize=*:350px')

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(_corona(client)) 

