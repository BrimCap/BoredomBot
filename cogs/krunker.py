import discord
from discord.ext import commands

import requests

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
            description = link
        )

        game.add_field(name = "Map", value = info[4]['i'])
        game.add_field(name = "Players", value = f"{info[2]} / {info[3]}", inline = True)

        send = await ctx.send(embed = game)

        while True:

            res = requests.get("https://matchmaker.krunker.io/game-info?game=" + gamelink)

            info = json.loads(res.text)

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
               description = link
            )

            update.add_field(name = "Map", value = info[4]['i'])
            update.add_field(name = "Players", value = f"{info[2]} / {info[3]}", inline = True)

            await send.edit(embed = update)

            await asyncio.sleep(5)

def setup(client):
    client.add_cog(Krunker(client))
