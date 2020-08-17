import discord
from discord.ext import commands, tasks

import datetime
from day import calc_day

import json

import traceback

class Exams(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.test_check.start()

    def calc_date(self, days_apart : datetime.timedelta):

        if days_apart == datetime.timedelta(days = 0):
            return 'Today'

        elif days_apart == datetime.timedelta(days = 1):
            return 'Tomorrow'

        elif days_apart == datetime.timedelta(days = 2):
            return 'Day after tomorrow'

        elif days_apart == datetime.timedelta(days = 7):
            return 'Next Week'

        else:
            return f"In {days_apart.days} days"

    @tasks.loop(hours = 24)
    async def test_check(self):

        await self.client.wait_until_ready()

        with open("DB/tests.json", "r") as f:
            tests = json.load(f)

        servers = discord.utils.get(self.client.guilds, name = 'SILENCED ROBO')
        channel = discord.utils.get(servers.channels, name = '📚-school')

        for test in tests:

            test_date = datetime.date(test['date']['year'], test['date']['month'], test['date']['day'])
            one_day = datetime.timedelta(days = 1)

            if datetime.date.today() == test_date - one_day and not test['reminded']:
                await channel.send(f"Hey @everyone! Tommorow you have **{test['subject']}**: **{test['lesson']}**! Just a reminder!")
                test['reminded'] = True

        with open("DB/tests.json", "w") as f:
            json.dump(tests, f, indent = 4)

    @commands.command(aliases = ['add'])
    async def add_test(self, ctx, subject, lesson : int, *, date):

        days = (
            'monday',
            'tuesday', 
            'wednesday', 
            'thursday', 
            'friday', 
            'saturday', 
            'sunday'
        )

        with open("DB/tests.json", "r") as f:
            tests = json.load(f)
        
        chech_hyphen = date.find('-')

        if chech_hyphen in [1, 2]:

            split = date.split('-')

            dates = [split[0], split[1], split[2]]
            
            await ctx.send(f"👌 Added **{subject}**: **{lesson}** on **{date}** 👌")

        else:
            if date.lower() in ['tomorrow', 'tommorrow', 'tommorow']:

                one_day = datetime.timedelta(days = 1)
                date = datetime.date.today() + one_day

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f'👌 Added **{subject}**: **{lesson}** on **{understandable_date}**')

            elif date.lower() == 'day after tomorrow':
                two_days = datetime.timedelta(days = 2)
                date = datetime.date.today() + two_days

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f'👌 Added **{subject}**: **{lesson}** on **{understandable_date}**')

            elif date.lower() in ['next week', 'one week']:
                one_week = datetime.timedelta(days = 7)
                date = datetime.date.today() + one_week

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f'👌 Added **{subject}**: **{lesson}** on **{understandable_date}**')

            elif date.lower() in days:
                date = calc_day(date.lower())

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f"👌 Added **{subject}**: **{lesson}** on **{understandable_date}**")

            elif date.lower().startswith('next') and date.lower().endswith(days):
                date = calc_day(date.lower()[5:], True)

                dates = [date.day, date.month, date.year]

                understandable_date = f"{date.day}-{date.month}-{date.year}"

                await ctx.send(f"👌 Added **{subject}**: **{lesson}** on **{understandable_date}**")

            else:
                await ctx.send('I dont quite know what you said there.. Did you spell something wrong...?')
                return

        tests.append({
            "subject": subject,
            "lesson": lesson,
            "date": {
                "day": int(dates[0]),
                "month": int(dates[1]),
                "year": int(dates[2])
            },
            "reminded": False
        })
                

        with open("DB/tests.json", "w") as f:
            json.dump(tests, f, indent = 4)


    @commands.command(aliases = ['delete_test', 'delete', 'remove', 'del'])
    async def remove_test(self, ctx, index : int = None):

        with open("DB/tests.json", "r") as f:
            tests = json.load(f)

        if index is not None:

            try:
                await ctx.send(f"👌 Removed **{tests[index]['subject']}**: **{tests[index]['lesson']}**")

            except IndexError:
                await ctx.send(f"Couldn't find the id of **{index}**")

            else:
                del tests[index]

        else:

            for i, test in enumerate(tests):
                test_date = datetime.date(test['date']['year'], test['date']['month'], test['date']['day'])

                if test_date <= datetime.date.today():
                    await ctx.send(f"👌 Removed **{test['subject']}**: **{test['lesson']}**")
                    del tests[i]

        with open("DB/tests.json", "w") as f:
            json.dump(tests, f, indent = 4)

    @commands.command(aliases = ['test'])
    async def tests(self, ctx):

        with open("DB/tests.json", "r") as f:
            tests = json.load(f)

        if len(tests) == 0:
            await ctx.send("No tests currently! Woohoo!")
            return

        for test_number, test in enumerate(tests):

            datetime_date = datetime.date(test['date']['year'], test['date']['month'], test['date']['day'])
            days_apart = datetime_date - datetime.date.today()

            show_date = self.calc_date(days_apart)

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

        with open("DB/tests.json", "r") as f:
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
