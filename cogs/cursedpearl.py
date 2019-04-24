import random

import discord
import giphypop
from discord.ext import commands

from .utils.dataIO import fileIO


class CursedPearl:
    def __init__(self, bot):
        self.bot = bot
        self.quotes = fileIO("data/cp/quotes/quotes.json", "load")
        self.author = fileIO("data/cp/quotes/author.json", "load")


    def serverCheck(self, ctx):
        if ctx.message.server.id == '515370084538253333':
            return True
        else: return False

    @commands.command(pass_context=True, no_pm=True)
    async def levels(self, ctx):
        if self.serverCheck(ctx):
            await self.bot.send_file(ctx.message.channel, "data/card.png")

    @commands.command(pass_context=True, no_pm=True)
    async def rank(self, ctx):
        if self.serverCheck(ctx):
            await self.bot.send_file(ctx.message.channel, "data/card.png")

    @commands.command(pass_context=True, no_pm=True)
    async def peridot(self, ctx):
        if self.serverCheck(ctx):
            g = giphypop.Giphy("KZciiXBwyJ9RabyZyUHjQ8e4ZutZQ1Go")
            results = [x for x in g.search('Peridot')]
            embed = discord.Embed(color=0xe6e200)
            embed.set_image(url=random.choice(results).raw_data['images']['fixed_height_downsampled']['url'])
            embed.set_footer(text="This is a random gif from Giphy using the search term 'Peridot'")
            await self.bot.say(embed=embed)

    @commands.command()
    async def quote(self):
        index = random.randint(0,len(self.quotes))
        quote = self.quotes[index]
        author = self.author[index]
        if 'Pearl' in author:
            thumbnail = 'https://i.lensdump.com/i/Agxrvq.png'
            color = 0xf7ceb2
        elif 'Garnet' in author:
            thumbnail = 'https://i.lensdump.com/i/AgxEca.png'
            color = 0x7a032d
        elif 'Amethyst' in author:
            thumbnail = 'https://i.lensdump.com/i/AgxtGA.png'
            color = 0xad8dbe
        elif 'Steven' in author:
            thumbnail = 'https://i.lensdump.com/i/AgxREM.png'
            color = 0xffc954
        elif 'Lapis' in author:
            thumbnail = 'https://i.lensdump.com/i/AgxTHQ.png'
            color = 0x66b9fb
        elif 'Peridot' in author:
            thumbnail = 'https://i.lensdump.com/i/AgxC3k.png'
            color = 0x3c796a

        embed = discord.Embed(title=quote, description='- ' + author, color=color)
        embed.set_thumbnail(url=thumbnail)
        self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(CursedPearl(bot))
