import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.command(description="Send a message for Genshin redemption codes with buttons.")
async def genshin(ctx, *, content):
    codes = content.split(",")

    code = ""

    check = "<a:check:1170116811564523581>"
    url_link = "<:url:1170116813569400853>"

    embed=discord.Embed(
        color=discord.Colour.dark_teal(),
        title="Active Codes",
        description=f"{url_link} [Redeemable by clicking below](https://genshin.mihoyo.com/en/gift) \n :mega: **Note**:  Codes expire quickly, so be sure to redeem them as soon as possible!")
    for code in codes:
        embed.add_field(name="", value=(f"{check} `{code}` | [Direct Link](https://genshin.hoyoverse.com/en/gift?code={code})"), inline=False)
    await ctx.send(embed=embed)


@bot.command(description="Send a message for Star Rail redemption codes with buttons.")
async def hsr(ctx, *, content):
    codes = content.split(",")

    code = ""

    check = "<a:check:1170116811564523581>"
    url_link = "<:url:1170116813569400853>"

    embed=discord.Embed(
        color=discord.Colour.dark_teal(),
        title="Active Codes",
        description=f"{url_link} [Redeemable by clicking below](https://hsr.hoyoverse.com/gift) \n :mega: **Note**:  Codes expire quickly, so be sure to redeem them as soon as possible!")
    for code in codes:
        embed.add_field(name="", value=(f"{check} `{code}` | [Direct Link](https://hsr.hoyoverse.com/gift?code={code})"), inline=False)
    await ctx.send(embed=embed)

@bot.command(description="Send a message for DBD redemption codes.")
async def dbd(ctx, *, content):
    codes = content.split(",")

    code = ""

    check = "<a:check:1170116811564523581>"
    url_link = "<:url:1170116813569400853>"

    embed=discord.Embed(
        color=discord.Colour.dark_teal(),
        title="Active Codes",
        description=f"{url_link} [Redeemable through in-game store \n :mega: **Note**:  Codes expire quickly, so be sure to redeem them as soon as possible!")
    for code in codes:
        embed.add_field(name="", value=(f"{check} `{code}`"), inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def sync(ctx):
    print("sync command")
    await bot.tree.sync()
    await ctx.send('Command tree synced.')

bot.run(TOKEN)