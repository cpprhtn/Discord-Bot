import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class CategoryManager(commands.Cog):
	"""
	운영진 역할을 가진 사용자들을 위한 카테고리 관리 명령어 모음
	- create_category: 카테고리를 생성합니다.
	- delete_category: 카테고리를 삭제합니다.
	- update_category: 카테고리를 수정합니다.
	"""
	def __init__(self, bot):
		self.bot = bot

	async def create_category(self, ctx):
		"""
		카테고리를 생성합니다.
		"""
		pass

def setup(bot):
	bot.add_cog(CategoryManager(bot))
	print("CategoryManager Cog is loaded")
