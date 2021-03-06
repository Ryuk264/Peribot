import json
import urllib.request

import discord
from discord.ext import commands


class XKCD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.apiurl = "http://xkcd.com/{x}/info.0.json"
        self.current = "http://xkcd.com/info.0.json"

    @commands.command()
    async def xkcd(self, ctx, number: int = None):
        """
        Get the current XKCD comic or a specific one
        :param number: Comic number
        :return: The comic you requested
        """
        if number is None:
            with urllib.request.urlopen(self.current) as url:
                data = json.loads(url.read().decode())
                embed = discord.Embed(title=data["title"], description=f"Alt: {data['alt']}")
                embed.set_image(url=data["img"])
                embed.set_footer(text=f"XKCD nr.{data['num']}")
                await ctx.send(embed=embed)
        else:
            try:
                with urllib.request.urlopen(self.apiurl.format(x=number)) as url:
                    data = json.loads(url.read().decode())
                    em = discord.Embed(title=data["title"],
                                       description=f"Alt: {data['alt']}")
                    em.set_image(url=data["img"])
                    em.set_footer(text=f"XKCD nr.{data['num']}")
                    await ctx.send(embed=em)
            except:
                await ctx.send("Could not find an XKCD with this ID!")

    # @xkcd.command()
    # async def id(self, ctx, number: int):
    #    with urllib.request.urlopen(self.apiurl.format(x = number)) as url:
    #        data = json.loads(url.read().decode())
    #        em = discord.Embed(title=data["title"], description="Alt: {x}".format(x = data["alt"], color=discord.Color.red()))
    #        em.set_image(url=data["img"])
    #        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(XKCD(bot))
