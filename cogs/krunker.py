import discord
from discord.ext import commands

import requests
import bs4

import json

import asyncio

class Krunker(commands.Cog):

    rotation_maps = [
        'Burg',
        'Littletown',
        'Sandstorm',
        'Subzero',
        'Undergrowth',
        'Shipyard',
        'Freight',
        'Lostworld',
        'Citadel',
        'Oasis',
        'Kanji',
        'Newtown',
        'Industry'
    ]

    def __init__(self, client):
        self.client = client
        self.playing = False

    @commands.Cog.listener()
    async def on_message(self, message):

        def remove_gamemode(game):

            game_split = game.split('_')

            gamemode = len(game_split[0]) + 1

            return game[gamemode:]

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

            if info[4]['m'] == 0:
                map_name = remove_gamemode(info[4]['i'])

                map_number = self.rotation_maps.index(map_name)

                game.set_image(url = 'https://krunker.io/img/maps/map_' + str(map_number) + '.png')

            else:
                game.set_image(url = 'https://user-assets.krunker.io/m' + str(info[4]['m']) + '/thumb.png?v=5')
            

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

                if info[4]['m'] == 0:
                    map_name = remove_gamemode(info[4]['i'])

                    map_number = self.rotation_maps.index(map_name)

                    update.set_image(url = 'https://krunker.io/img/maps/map_' + str(map_number) + '.png')

                else:
                    update.set_image(url = 'https://user-assets.krunker.io/m' + str(info[4]['m']) + '/thumb.png?v=5')

                await send.edit(embed = update)

                await asyncio.sleep(20)

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
