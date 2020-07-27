import discord
from discord.ext import commands

import os
import json

os.chdir(r'C:\Users\Vandith Krishna\Desktop\Stuff\MyStuff\Code\Python\Discord\Discord Bots\BoredomBot\cogs')

class Levels(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def update_users(self, users, user):

        user_id = str(user.id)

        if not user_id in users:
            users[user_id] = {}
            users[user_id]["money"] = 0

    async def add_money(self, users, user, money):

        user_id = str(user.id)

        users[user_id]["money"] += money

    @commands.Cog.listener()
    async def on_message(self, message):

        with open("user_levels.json", "r") as f:
            users = json.load(f)

        await self.update_users(users, message.author)
        await self.add_money(users, message.author, 1)

        with open("user_levels.json", "w") as f:
            json.dump(users, f, indent = 4)

    @commands.command(aliases = ['rank', 'level', 'cash'])
    async def money(self, ctx, member : discord.Member = None):

        with open("user_levels.json", "r") as f:
            users = json.load(f)

        member = ctx.author if not member else member

        member_id = str(member.id)

        rank = discord.Embed(
            color = 0x0dc700,
            description = f"**MONEY:** {users[member_id]['money']}"
        )

        rank.set_author(name = member.name, icon_url = member.avatar_url)

        await ctx.send(embed = rank)

def setup(client):
    client.add_cog(Levels(client))
