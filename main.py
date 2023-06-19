import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from dotenv import load_dotenv
import os
from pyfiglet import Figlet
import asyncio





@slash.slash(name="ascii", description="Generate ASCII art from text")
async def ascii(ctx: SlashContext, text: str):
    f = Figlet(font='standard')
    ascii_art = f.renderText(text)
    await ctx.send(f"```\n{ascii_art}\n```")






@bot.event
async def on_slash_command_error(ctx, ex):
    await ctx.send(str(ex))

bot.run(TOKEN)
