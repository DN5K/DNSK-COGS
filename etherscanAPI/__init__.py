from .etherscanAPI import ES

from redbot.core.bot import Red

async def setup(bot: Red) -> None:
    cog = ES(bot)
    #await cog.initialize()
    bot.add_cog(cog)
