import discord
import sys
import os
from discord.ext import commands
from .config import TOKEN, PREFIX, EXTENSIONS

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'discord_bot')))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
	for extension in EXTENSIONS:
		try:
			await bot.load_extension(extension)
		except Exception as e:
			print(f'Failed to load extension {extension}.', file=sys.stderr)
			print(e)

def run_bot():
	if TOKEN is None:
		raise ValueError("Discord Token is not set. Please set Token in config.py")
	bot.run(TOKEN)