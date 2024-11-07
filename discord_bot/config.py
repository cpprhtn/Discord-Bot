import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX") 

EXTENSIONS = [
	f"discord_bot.cogs.{manager}.{cog[:-3]}"
	for manager in os.listdir("discord_bot/cogs")
	if os.path.isdir(f"discord_bot/cogs/{manager}")
	for cog in os.listdir(f"discord_bot/cogs/{manager}")
	if cog.endswith(".py") and cog != "__init__.py"
]
