from .coingecko import CoinGecko

from redbot.core.bot import Red

async def setup(bot: Red) -> None:
    cog = CoinGecko(bot)
    await cog.initialize()
    bot.add_cog(cog)
