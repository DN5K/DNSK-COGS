from .coingecko import CoinGecko

from redbot.core import commands

import discord



@commands.command()
async def hoge_status_updater(self, ctx):
    await self.getdata(coin="hoge-finance")
    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'Hoge: ${price:,.6f}'))