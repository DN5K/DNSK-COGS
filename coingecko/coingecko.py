# Import CoinGeckoAPI
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

from datetime import datetime

from redbot.core import commands
from redbot.core.utils.chat_formatting import humanize_timedelta

import json
import discord
import dateutil.parser



class CoinGecko(commands.Cog):
    """CoinGecko for RedBot"""
    
    
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pingcg(self, ctx):
        """Ping the CoinGecko API"""
        ping = cg.ping()
        ping_response = ping["gecko_says"]
        await ctx.send(f"CoingGeckoAPI is up and running!\n**{ping_response}**")

    @commands.command()
    async def getprice(self, ctx, coin, amount: float = 1.0,):
        """Fetch the price of a Coin"""

        # trigger get data for coin
        #try:
        await self.getdata(coin)
        #except:
        #    await ctx.send("Something went wrong. Make sure to use a proper coin ID!")
        #    return None

        # setup embed
        calc = price*amount
        if amount == 1:
            amount_price = f"{calc:,.8f}"
        else:
            amount_price = f"{calc:,.2f}"
        
        msg = f"```fix\n{amount:,.0f} {coin_name}\n= ${amount_price}```\n"
        embed = discord.Embed(description=msg, colour=discord.Colour.blue())
        embed.set_author(name=coin_name, url="https://www.coingecko.com/en/coins/"f"{coin_id}", icon_url=image)
        embed.set_footer(text="Powered by CoinGecko API", icon_url="https://www.coingecko.com/favicon-96x96.png")
        embed.timestamp = last_updated
        
        hour_1_emoji = "<:greenarrow:835522230452092969>" if price1h >= 0 else "<:redarrow:835522249942630410>"
        hour_24_emoji = "<:greenarrow:835522230452092969>" if price24h >= 0 else "<:redarrow:835522249942630410>"
        if price7d == "N/A":
            days_7_emoji = ":question:"
        else:
            days_7_emoji = "<:greenarrow:835522230452092969>" if price7d >= 0 else "<:redarrow:835522249942630410>"
        
        if amount == 1:
            embed.set_thumbnail(url=image)
            embed.add_field(name="Change 1 hour " + hour_1_emoji, value=f"`{price1h}%`", inline = True)
            embed.add_field(name="Change 24 hours " + hour_24_emoji, value=f"`{price24h}%`", inline = True)
            embed.add_field(name="Change 7 days " + days_7_emoji, value=f"`{price7d}%`\n\n\n", inline = True)
            embed.add_field(name="_ _", value="_ _", inline = False)
            embed.add_field(name="Market Cap  :moneybag:", value=f"`${market_cap:,.0f}`\n\n", inline = True)
            embed.add_field(name="24 Hour Volume  :calendar:", value=f"`${vol24h:,.0f}`\n\n", inline = True)
            if coin == "hoge":
                burned_supply = f"{1000000000000 - circulating_supply:,.0f}"
                embed.add_field(name="_  _", value="_ _", inline = False)
                embed.add_field(name="Circulating Supply  :repeat:", value=f"`{circulating_supply:,.0f}`", inline = True)
                embed.add_field(name="Burned Supply  :fire:", value=f"`{burned_supply}`", inline = True)
                embed.add_field(name="_   _", value="_ _", inline = False)
            else:
                pass
        else:
            pass
            
            msg += (
            f"Market Cap: **{market_cap}**\n"
            f"24 Hour Volume: **{vol24h}**\n"
            f"Total Supply: **1000000000000**\n"
            f"Circulating Supply: **{circulating_supply}**\n"
            f"Change 1 hour{hour_1_emoji}: **{price1h}%**\n"
            f"Change 24 hours{hour_24_emoji}: **{price24h}%**\n"
            f"Change 7 days{days_7_emoji}: **{price7d}%**\n")

        # send embed
        await ctx.send(embed=embed)
        #await ctx.send(f"{name}s current price: ${price}\n 1h%: {price1h}\n 24h%: {price24h}\n 7d%: {price7d}")
    
    
    
    
#-#-#-#-#-# FUNCTIONS #-#-#-#-#-# 
    
    
    
### get coin data
    async def getdata(self, coin):
        
        # name alias
        if coin == "hoge":
            coin = "hoge-finance"
        elif coin == "comfy":
            coin = "comfytoken"
        elif coin == "btc":
            coin = "bitcoin"
        elif coin == "eth":
            coin = "ethereum"
        elif coin == "bnb":
            coin = "binancecoin"
        else:
            pass
        
        # run CoinGeckoAPI /coins/{id}
        data = cg.get_coin_by_id(
            id = coin,
            localization = "false",
            tickers = "true",
            market_data = "true",
            community_data = "false",
            developer_data = "false",
            sparkline = "false")
        
        # get values from json (data) and make them global
        global coin_id, coin_name, image, price, market_cap, vol24h, price1h, price24h, price7d, ath, ath_date, circulating_supply, last_updated
        coin_id = data["id"]
        coin_name = data["name"]
        image = data["image"]["large"]
        price = data["market_data"]["current_price"]["usd"]
        market_cap = data["market_data"]["market_cap"]["usd"]
        vol24h = data["market_data"]["total_volume"]["usd"]
        price1h = data["market_data"]["price_change_percentage_1h_in_currency"]["usd"]
        price24h = data["market_data"]["price_change_percentage_24h_in_currency"]["usd"]
        try:
            price7d = data["market_data"]["price_change_percentage_7d_in_currency"]["usd"]
        except:
            price7d = "N/A"
        ath = data["market_data"]["ath"]["usd"]
        ath_date = data["market_data"]["ath_date"]["usd"]
        circulating_supply = data["market_data"]["circulating_supply"]
        last_updated = datetime.strptime(data["last_updated"], "%Y-%m-%dT%H:%M:%S.%fZ")
        
        # replace empty values with N/A
        
