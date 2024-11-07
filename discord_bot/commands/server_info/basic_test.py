from discord.ext import commands

def server_ping(bot):
	"""
	Ping the server
	서버의 응답 시간을 확인합니다.
	"""
	@bot.command(name="ping")
	async def ping(ctx):
		latency = round(bot.latency * 1000)
		await ctx.send(f"Pong! {latency}ms")
