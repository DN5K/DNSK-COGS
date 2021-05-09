from .helpmenu import HelpMenu

from redbot.core.bot import Red

async def setup(bot: Red) -> None:
    cog = HelpMenu(bot)
    bot.add_cog(cog)
