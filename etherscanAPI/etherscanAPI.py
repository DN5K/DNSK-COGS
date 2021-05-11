from __future__ import division

from etherscan import Etherscan
eths = Etherscan("K6M6E3NKN5P9TGHU5JYZ5MPYZ5Z2H23G8D") # key in quotation marks

from datetime import datetime

import discord
import contextlib
from redbot.core import Config, commands
from redbot.core.utils.menus import menu, commands, DEFAULT_CONTROLS





class ES(commands.Cog):
    """HelpMenu for Hoge"""
    
    
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gt"])
    async def gastracker(self, ctx):
        data = eths.get_gas_oracle()
        dataprice = eths.get_eth_last_price()
        
        lowgas = data["SafeGasPrice"]
        averagegas = data["ProposeGasPrice"]
        highgas = data["FastGasPrice"]
        
        ethprice = dataprice["ethusd"]
        gwei = 0.000000001
        lowprice = float(ethprice) * gwei * float(lowgas) * 200000
        averagepice = float(ethprice) * gwei * float(averagegas) * 200000
        highprice = float(ethprice) * gwei * float(highgas) * 200000
        
        msg = f"```prolog\nCURRENT ETH GAS PRICES. ESTIMATED UNISWAP SWAP COST.```\n"
        embed = discord.Embed(description=msg, colour=discord.Colour.blue())
        embed.set_author(name="Ethereum Gas Tracker", url="https://etherscan.io/gastracker", icon_url="https://etherscan.io/images/brandassets/etherscan-logo-light-circle.png")
        embed.set_footer(text="Powered by Etherscan.io APIs")
        
        embed.add_field(name=":slight_smile: Low:", value=f"{lowgas} gwei\n${lowprice:,.2f}", inline = True)
        embed.add_field(name=":confused: Average:", value=f"{averagegas} gwei\n${averagepice:,.2f}", inline = True)
        embed.add_field(name=":tired_face: High:", value=f"{highgas} gwei\n${highprice:,.2f}", inline = True)
        embed.add_field(name="_ _", value="_ _", inline = False)
        
        await ctx.send(embed=embed)
