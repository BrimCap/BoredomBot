import discord
from discord.ext import commands, tasks

import datetime

import json

class Exams(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def add_test(self, ctx, subject, lesson : int, date):
        
        nice_date = f"{date[0:2]}-{date[2:4]}-{date[4:]}"
        
        with open("tests.json", "r") as f:
            tests = json.load(f)

        tests.append({
            "subject": subject,
            "lesson": lesson,
            "date": {
                "day": int(date[0:2]),
                "month": int(date[2:4]),
                "year": int(date[4:])
            }
        })

        with open("tests.json", "w") as f:
            json.dump(tests, f, indent = 4)

        await ctx.send(f"Added **{subject}**: **{lesson}** on **{nice_date}** 👌")

    @commands.command(aliases = ['delete_test'])
    async def remove_test(self, ctx, index : int):

        with open("tests.json", "r") as f:
            tests = json.load(f)

        await ctx.send(f"Removed **{tests[index]['subject']}**: **{tests[index]['lesson']}**")
        del tests[index]

        with open("tests.json", "w") as f:
            json.dump(tests, f, indent = 4)

    @commands.command(aliases = ['test'])
    async def tests(self, ctx):

        with open("tests.json", "r") as f:
            tests = json.load(f)

        if len(tests) == 0:
            await ctx.send("No tests currently! Woohoo!")
            return

        for test_number, test in enumerate(tests):

            datetime_date = datetime.date(test['date']['year'], test['date']['month'], test['date']['day'])

            that_test = discord.Embed(
                color = 0x21eded,
                title = f"{test['subject']}: {test['lesson']}"
            )

            that_test.add_field(name = "ID", value = test_number)
            that_test.add_field(name = "Due Date", value = datetime_date)

            await ctx.send(embed = that_test)

def setup(client):
    client.add_cog(Exams(client))