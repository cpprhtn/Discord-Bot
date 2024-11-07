import discord
from discord.ext import commands
from .config import TOKEN, PREFIX
from .commands.server_info.basic_test import server_ping
from .commands.server_info.server_info import setup_info_commands

bot =  commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

server_ping(bot)
setup_info_commands(bot)

def run_bot():
	if TOKEN is None:
		raise ValueError("Discord Token is not set. Please set Token in config.py")
	bot.run(TOKEN)