from .cg import CoinGecko


def setup(bot):
    bot.add_cog(CoinGecko(bot))