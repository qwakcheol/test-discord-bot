""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""
import discord 

from discord.ext import commands
from discord.ext.commands import Context


# Here we name the cog and create a new class for the cog.
class Store(commands.Cog, name="store"):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_group(
        name="buy",
        description="Spend mileage points to buy items"
    )
    async def buy(self, context: Context) -> None:
        """
        Deduct mileage points from DB and sell user items
        """
        if context.invoked_subcommand is None:
            embed = discord.Embed(
                description="Please specify an item you'd like to purchase.",
                color=0xE02B2B,
            )
            await context.send(embed=embed)

    @buy.command(
        name="coffee",
        description="Buy coffee for 10 mileage points"
    )
    async def coffee(self, context: Context) -> None:
        coffee = 10
        embed = discord.Embed(
            title="Here's your coffee!",
            description=f"You've bought coffee using {coffee} mileage points!",
            color=0xBEBEFE
        )
        await context.send(embed=embed)

    @buy.command(
        name="iffy",
        description="Buy Iffy's time for 10000 mileage points"
    )
    async def iffy(self, context: Context) -> None:
        iffy = 10000
        embed = discord.Embed(
            title="Here's Iffy's time!",
            description=f"You've bought Iffy's time using {iffy} mileage points!",
            color=0xBEBEFE
        )
        await context.send(embed=embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Store(bot))
