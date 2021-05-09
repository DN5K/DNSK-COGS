import discord
import contextlib
from redbot.core import Config, commands
from redbot.core.utils.menus import menu, commands, DEFAULT_CONTROLS





class HelpMenu(commands.Cog):
    """HelpMenu for Hoge"""
    
    
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["hm"])
    async def helpmenu(self, ctx):
        """Open the Help Menu"""

        ## BUILD EMBED
        # MAIN
        #msg = "**__Click the corresponding number of the topic you need help with.__**"
        embed_main = discord.Embed(colour=discord.Colour.blue())
        embed_main.set_author(name="HELPMENU", icon_url="https://nation.hoge.finance/styles/hoge/hoge.png")
        embed_main.set_footer(text="ℹ️ Click the corresponding number of the topic you need help with.")

        # PAGES
        embed_pages = discord.Embed(colour=discord.Colour.blue())
        embed_pages.set_author(name="HELPMENU", icon_url="https://nation.hoge.finance/styles/hoge/hoge.png")
        embed_pages.set_footer(text="\n⬅️ Main menu\n❌ Close menu")

        # MAIN MENU
        embeds_main = []
        
        embed_main.add_field(name=":one: - Introduction", value="*Introduction to our Discord Server.*", inline = False)
        embed_main.add_field(name=":two: - About Hoge Finance", value="*Basic Information about Hoge Finance.*", inline = False)
        embed_main.add_field(name=":three: - How to buy", value="*Information on how and where to buy Hoge.*", inline = False)
        embeds_main.append(embed_main)

        # PAGES
        embeds_pages = []


        
        ## BUILD PAGES
        async def closemenu(ctx, pages, controls, message, page, timeout, emoji):
            with contextlib.suppress(discord.NotFound):
                await message.delete()
        
        async def mainmenu(ctx, pages, controls, message, page, timeout, emoji):
            await menu(ctx, pages=embeds_main, controls=menu_base, message=None, page=0, timeout=300)
        
        
        async def page_one(ctx, pages, controls, message, page, timeout, emoji):
            # build embed
            embed_pages.clear_fields()
            embed_pages.add_field(name=":one: **__Introduction__**", value="This is a basic introduction. blab lab lblalbal", inline = False)
            embeds_pages.append(embed_pages)
            # send embed
            await menu(ctx, pages=embeds_pages, controls=menu_page, message=None, page=0, timeout=300)
        
        async def page_two(ctx, pages, controls, message, page, timeout, emoji):
            # build embed
            embed_pages.clear_fields()
            embed_pages.add_field(name="Test2", value="This shows you stuff about Y", inline = False)
            embeds_pages.append(embed_pages)
            # send embed
            await menu(ctx, pages=embeds_pages, controls=menu_page, message=None, page=0, timeout=300)
        
        async def page_three(ctx, pages, controls, message, page, timeout, emoji):
            # build embed
            embed_pages.clear_fields()
            embed_pages.add_field(name="Test3", value="This shows you stuff about Z", inline = False)
            embeds_pages.append(embed_pages)
            # send embed
            await menu(ctx, pages=embeds_pages, controls=menu_page, message=None, page=0, timeout=300)



        ## REACTIONS MENU CONTROL - USE "KEYCAP DIGIT X" FOR NUMBER EMOJI
        # MAIN MENU (NUMBERS ONLY)
        menu_base = {"1️⃣": page_one,
                     "2️⃣": page_two,
                     "3️⃣": page_three,
                     "❌": closemenu}
        # PAGE MENU (MAIN MENU BUTTON)
        menu_page = {"⬅️": mainmenu,
                     "❌": closemenu}


        ## SEND INITIAL MENU
        await menu(ctx, pages=embeds_main, controls=menu_base, message=None, page=0, timeout=300)