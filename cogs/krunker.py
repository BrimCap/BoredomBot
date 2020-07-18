import discord
from discord.ext import commands

import requests

import json

import asyncio

class Krunker(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.playing = False

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content.startswith('https://krunker.io/?game='):

            self.playing = True

            link = message.content

            gamelink = link[25:]

            await message.delete()

            res = requests.get("https://matchmaker.krunker.io/game-info?game=" + gamelink)

            info = json.loads(res.text)

            game = discord.Embed(
                colour = 0xfad15f,
                title = 'Krunker Game Invite',
                description = link
            )

            game.add_field(name = "Map", value = info[4]['i'])
            game.add_field(name = "Players", value = f"{info[2]} / {info[3]}", inline = True)

            send = await message.channel.send(embed = game)

            while self.playing:

                res = requests.get("https://matchmaker.krunker.io/game-info?game=" + gamelink)

                info = json.loads(res.text)

                if res.text == '{"error":"InvalidGameId"}':
                
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

            end_message = discord.Embed(
                colour = 0xfad15f,
                description = 'The game end or was closed. Sad'
            )

            await send.edit(embed = end_message)

    @commands.command(aliases = ['stop'])
    async def close(self, ctx):
        if not self.playing:
            await ctx.send('No active game found')
            return

        else:
            self.playing = False

def setup(client):
    client.add_cog(Krunker(client))
