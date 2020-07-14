import discord
from discord.ext import commands

import requests
import bs4

import json

import asyncio

class Krunker(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['krunk', 'invite', 'k', 'play'])
    async def krunker(self, ctx, link):

        if not link.startswith('https://krunker.io'):
            await ctx.send("This is not a valid link. Sad")
            return

        gamelink = link[25:]

        await ctx.message.delete()

        res = requests.get("https://matchmaker.krunker.io/game-info?game=" + gamelink)

        info = json.loads(res.text)

        game = discord.Embed(
            colour = 0xfad15f,
            title = 'Krunker Game Invite',
            description = f'''{link}
            
            Map: {info[4]['i']}
            Players: {info[2]} / {info[3]}
            '''
        )

        send = await ctx.send(embed = game)

        while True:

            res = requests.get("https://matchmaker.krunker.io/game-info?game=" + gamelink)

            if res.text == '{"error":"InvalidGameId"}':
                
                end_message = discord.Embed(
                    colour = 0xfad15f,
                    description = 'The game end. Sad'
                )

                await send.edit(embed = end_message)
                break
                

            update = discord.Embed(
               colour = 0xfad15f,
               title = 'Krunker Game Invite',
               description = f'''{link}

               Map: {info[4]['i']}
               Players: {info[2]} / {info[3]}
               '''
            )

            await send.edit(embed = update)

            await asyncio.sleep(5)

        await send.send(embed = end_message)

def setup(client):
    client.add_cog(Krunker(client))
