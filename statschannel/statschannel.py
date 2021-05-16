from ethplorer.token import Token

import json
import discord
import dateutil.parser
import logging
import asyncio
import time

from datetime import datetime

from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import humanize_timedelta


log = logging.getLogger("red.dsnk-cogs.statschannel")

class StatsChannel(commands.Cog):
    """Stats Channels"""



    def __init__(self, bot):
        self.bot = bot
        self.bg_loop_task = None

    @commands.command(aliases=["sc"])
    @checks.admin()
    async def statschannel(self, ctx, catID):
        await self.getdata(ctx)
        # GET CATEGORY
        getcategory = discord.utils.get(ctx.guild.categories, id=int(catID))

        #await ctx.send(f"{members}, {holders}\n{getcategory}")
        await ctx.guild.create_voice_channel(name=f"👥 Members: {members}", category=getcategory)
        await ctx.guild.create_voice_channel(name=f"🤲 Holders: {holders}", category=getcategory)



    @commands.command(aliases=["uc"])
    @checks.admin()
    async def updatechannels(self, ctx):
        await self.getdata(ctx)
        for channel in ctx.guild.channels:
            if "Members:" in channel.name:
                wanted_channel_id = channel.id
                await channel.edit(name=f"👥 Members: {members}")
            if "Holders:" in channel.name:
                wanted_channel_id = channel.id
                await channel.edit(name=f"🤲 Holders: {holders}")
        #await ctx.send(wanted_channel_id) # this is just to check



    async def getdata(self, ctx):
        global members, holders
        members = ctx.guild.member_count
        
        call = Token(address="0xfAd45E47083e4607302aa43c65fB3106F1cd7607")
        data = call.get_token_info()
        holders = data["holdersCount"]