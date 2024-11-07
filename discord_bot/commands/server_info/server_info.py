import discord
from discord.ext import commands

def setup_info_commands(bot):
	"""
	서버의 정보(서버 이름, 멤버수)를 가져옵니다.
	"""
	@bot.command(name="serverinfo")
	async def server_info(ctx):
		guild = ctx.guild
		embed = discord.Embed(title="서버 정보", color=discord.Color.blue())
		embed.add_field(name="서버 이름", value=guild.name, inline=False)
		embed.add_field(name="멤버 수", value=guild.member_count, inline=False)
		embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
		await ctx.send(embed=embed)