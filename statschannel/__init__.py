from .statschannel import StatsChannel

from redbot.core.bot import Red

async def setup(bot: Red) -> None:
    cog = StatsChannel(bot)
    bot.add_cog(cog)