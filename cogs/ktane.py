import discord
from discord.ext import commands

class Ktane(commands.Cog):

    battery = 0
    frk = False
    car = False
    serial = None

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setup(self, ctx):

        global battery, frk, car, serial

        await ctx.send('How many batteries are in the bomb')

        def battery(message : discord.Message):
            return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id and message.content

        battery_call = await self.client.wait_for('message', check = battery)

        battery = int(battery_call.content)

        await ctx.send(f'{battery} battries registerd')

        await ctx.send('is there a lit indicator saying FRK?')

        def FRK(message : discord.Message):
            return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id and message.content.lower()

        FRK = await self.client.wait_for('message', check = FRK)

        if FRK.content == 'yes':
            frk = True
            await ctx.send('**FRK** registerd')
        else:
            frk = False
            await ctx.send('No **FRK**')

        await ctx.send('Is there a lit indicator saying CAR?')

        def CAR(message : discord.Message):
            return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id and message.content.lower()

        CAR = await self.client.wait_for('message', check = CAR)

        if CAR.content == 'yes':
            car = True
            await ctx.send('**CAR** registerd')
        else:
            car = False
            await ctx.send('no **CAR**')

        await ctx.send('What is the serial number?')

        def serial(message : discord.Message):
            return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id and message.content

        SERIAL_CALL = await self.client.wait_for('message', check = serial)

        serial = str(SERIAL_CALL.content.upper())

        await ctx.send('The serial has been registerd')

        await ctx.send("The bomb has been setup! Ready for modules.")

    @commands.command()
    async def button(self, ctx, color, text):
        
        global battery, car, frk

        accepted_colors = [
            'blue',
            'red',
            'white', 
            'yellow', 
            'black'
        ]

        accepted_text = [
            'abort', 
            'detonate',
            'hold',
            'press'
        ]

        if not color.lower() in accepted_colors:
            await ctx.send('This is not a valid color :/')
            return

        if not text.lower() in accepted_text:
            await ctx.send('This is not valid text :/')
            return

        async def hold(color):
            if color == 'blue':
                await ctx.send('Release when the countdown timer has a **4** in any position')

            elif color == 'white':
                await ctx.send('Release when the countdown timer has a **1** in any position')
                
            elif color == 'yellow':
                await ctx.send('Release when the countdown timer has a **5** in any position')
            
            else:
                await ctx.send('Release when the countdown timer has a **1** in any position')

        def color_side(message : discord.Message):
                return message.author.id == ctx.author.id and message.channel.id == ctx.channel.id and message.content.lower()

        if color == 'blue' and text == 'abort':
            await ctx.send('Hold the button down. What color does it show?')

            colour = await self.client.wait_for('message', check = color_side)

            await hold(colour.content)

        elif text == 'detonate' and battery > 1:
                await ctx.send('Press and relase the button')

        elif color == 'white' and car:

            await ctx.send('Hold the button down. What color does it show?')

            white_color = await self.client.wait_for('message', check = color_side)

            await hold(white_color.content)

        elif battery > 2 and frk:
            await ctx.send('Press and release the button')

        elif color == 'yellow':

            await ctx.send('Hold the button down. What color does it show?')

            yellow_color = await self.client.wait_for('message', check = color_side)

            await hold(yellow_color.content)

        elif color == 'red' and text == 'hold':

            await ctx.send('Press and release the button.')

        else:

            await ctx.send('Hold the button down. What color does it show?')

            last_color = await self.client.wait_for('message', check = color_side)

            await hold(last_color.content)


    @commands.command()
    async def wire(self, ctx, *, wire):

        global serial

        last = int(serial[-1]) % 2

        wires = wire.split()

        if len(wires) == 3:
            if 'red' not in wires:
                await ctx.send('Cut the second wire')

            elif wires[-1] == 'white':
                await ctx.send('Cut the last wire')

            elif wires.count('blue') > 1:
                await ctx.send('Cut the last blue wire.')

            else:
                await ctx.send('Cut the last wire')

        elif len(wires) == 4:
            if wires.count('red') > 1 and last == 1:
                await ctx.send('cut the last red wire')

            elif wires[-1] == 'yellow' and wires.count('red') == 0:
                await ctx.send('Cut the first wire')

            elif wires.count('blue') == 1:
                await ctx.send('Cut the first wire')

            elif wires.count('yellow') > 1:
                await ctx.send('Cut the last wire')

            else:
                await ctx.send('Cut the second wire')

        elif len(wires) == 5:
            if wires[-1] == 'black' and last == 1:
                await ctx.send('Cut the fourth wire')

            elif wires.count('red') == 1 and wires.count('yellow') > 1:
                await ctx.send('Cut the first wire')

            elif wires.count('black') == 0:
                await ctx.send('Cut the second wire')

            else:
                await ctx.send('Cut the second wire')

        elif len(wires) == 6:
            if wires.count('yellow') == 0 and last == 1:
                await ctx.send('Cut the third wire')

            elif wires.count('yellow') == 1 and wires.count('white') > 1:
                await ctx.send('Cut the fourth wire')
            
            elif wires.count('red') == 0:
                await ctx.send('Cut the last wire')

            else:
                await ctx.send('Cut the fourth wire')

        else:
            await ctx.send('That is not a valid wire combination :/')

    @commands.command()
    async def reset(self, ctx):
        global battery, car, frk, serial

        battery = 0
        car = False
        frk = False
        serial = None

        await ctx.send('Bomb has been reset! Hope you won that game. If not its because you **SUCK**')

def setup(client):
    client.add_cog(Ktane(client))