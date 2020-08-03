import discord
from discord.ext import commands, tasks

import datetime

import json

import traceback

class Exams(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.test_check.start()

    @tasks.loop(hours = 24)
    async def test_check(self):

        await self.client.wait_until_ready()

        with open("tests.json", "r") as f:
            tests = json.load(f)

        servers = discord.utils.get(self.client.guilds, name = 'SILENCED ROBO')
        channel = discord.utils.get(servers.channels, name = '📚-school')

        for test in tests:

            test_date = datetime.date(test['date']['year'], test['date']['month'], test['date']['day'])
            one_day = datetime.timedelta(days = 1)

            if datetime.date.today() == test_date - one_day:
                await channel.send(f"Hey @everyone! Tommorow you have **{test['subject']}**: **{test['lesson']}**! Just a reminder!")

    @commands.command(aliases = ['add'])
    async def add_test(self, ctx, subject, lesson : int, *, date):

        with open("tests.json", "r") as f:
            tests = json.load(f)
        
        chech_hyphen = date.find('-')

        if chech_hyphen in [1, 2]:

            split = date.split('-')

            dates = [split[0], split[1], split[2]]
            
            await ctx.send(f"Added **{subject}**: **{lesson}** on **{date}** 👌")

        else:
            if date.lower() in ['tomorrow', 'tommorrow', 'tommorow']:

                one_day = datetime.timedelta(days = 1)
                date = datetime.date.today() + one_day

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f'Added **{subject}**: **{lesson}** on **{understandable_date}**')

            elif date.lower() == 'day after tomorrow':
                two_days = datetime.timedelta(days = 2)
                date = datetime.date.today() + two_days

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f'Added **{subject}**: **{lesson}** on **{understandable_date}**')

            elif date.lower() in ['next week', 'one week']:
                one_week = datetime.timedelta(days = 7)
                date = datetime.date.today() + one_week

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f'Added **{subject}**: **{lesson}** on **{understandable_date}**')

            else:
                await ctx.send('I can only go upto one week. Not too smart I know, maybe you spelled something wrong?')

        tests.append({
            "subject": subject,
            "lesson": lesson,
            "date": {
                "day": int(dates[0]),
                "month": int(dates[1]),
                "year": int(dates[2])
            }
        })
                

        with open("tests.json", "w") as f:
            json.dump(tests, f, indent = 4)


    @commands.command(aliases = ['delete_test', 'delete', 'remove'])
    async def remove_test(self, ctx, index : int):

        with open("tests.json", "r") as f:
            tests = json.load(f)

        if index - 1 > len(tests):
            await ctx.send("Coudn't find that test :(\nTry Checking `!b tests` again")
            return
        
        else:
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
            days_apart = datetime_date - datetime.date.today()

            if days_apart == datetime.timedelta(days = 0):
                show_date = 'Today'
            
            elif days_apart == datetime.timedelta(days = 1):
                show_date = 'Tomorrow'

            elif days_apart == datetime.timedelta(days = 2):
                show_date = 'Day After Tomorrow'

            elif days_apart == datetime.timedelta(days = 7):
                show_date = 'Next Week'

            else:
                show_date = f'In {days_apart.days} days'

            that_test = discord.Embed(
                color = 0x21eded,
                title = f"{test['subject']}: {test['lesson']}"
            )

            that_test.add_field(name = "ID", value = test_number)
            that_test.add_field(name = "Due Date", value = show_date)

            await ctx.send(embed = that_test)

    @commands.command(aliases = ['tommorow', 'tomorrow'])
    async def check(self, ctx):

        sent = False

        with open("tests.json", "r") as f:
            tests = json.load(f)

        for test in tests:

            test_date = datetime.date(test['date']['year'], test['date']['month'], test['date']['day'])
            one_day = datetime.timedelta(days = 1)

            if datetime.date.today() == test_date - one_day:
                sent = True
                await ctx.send(f"Hey @everyone! Tommorow you have {test['subject']}: {test['lesson']}! Just a reminder!")

        if not sent:
            await ctx.send('Looks like there are no tests tomorrow! yay!')


def setup(client):
    client.add_cog(Exams(client))