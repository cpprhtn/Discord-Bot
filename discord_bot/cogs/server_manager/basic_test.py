import discord
from discord.ext import commands

class BasicTest(commands.Cog):
	"""
	기본적인 서버 테스트 명령어 모음
	"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping", help="Ping the server to check latency.")
	async def ping(self, ctx):
		"""
		Ping the server
		서버의 응답 시간을 확인합니다.
		"""
		latency = round(self.bot.latency * 1000)
		await ctx.send(f"Pong! {latency}ms")
	
	@commands.command(name="serverinfo", help="Get server information.")
	async def server_info(self, ctx):
		guild = ctx.guild
		embed = discord.Embed(title="서버 정보", color=discord.Color.blue())
		embed.add_field(name="서버 이름", value=guild.name, inline=False)
		embed.add_field(name="멤버 수", value=guild.member_count, inline=False)
		embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
		await ctx.send(embed=embed)

async def setup(bot):
	await bot.add_cog(BasicTest(bot))
	print("BasicTest Cog is loaded")