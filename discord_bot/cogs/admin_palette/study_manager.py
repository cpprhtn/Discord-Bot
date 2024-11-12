import discord
from discord.ext import commands
from discord.commands import slash_command
from datetime import datetime

class StudyManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Create a study room with roles and channels")
    @commands.has_permissions(administrator=True)
    async def create_study(self, ctx, study_name: str, season: str, category_name: str = None):
        guild = ctx.guild
        season = season.lower()
        year_short = datetime.now().strftime("%y")
        year_long = datetime.now().strftime("%Y")
        
        role_name = f"{year_short}-{season}-{study_name}"
        role = discord.utils.get(guild.roles, name=role_name)
        if role:
            await ctx.send(f"'{role_name}' 역할이 이미 존재합니다.")
            return

        category = discord.utils.get(guild.categories, name=category_name) if category_name else None
        if not category:
            category = await guild.create_category(name=category_name or "스터디")

        try:
            role = await guild.create_role(name=role_name)
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                role: discord.PermissionOverwrite(view_channel=True),
            }

            study_category = await guild.create_category(name=role_name, overwrites=overwrites)
            await guild.create_text_channel(f"{study_name}-채팅", category=study_category)
            await guild.create_voice_channel(f"{study_name}-음성", category=study_category)

            await ctx.send(f"'{role_name}' 스터디 카테고리와 역할이 생성되었습니다.")
        except discord.DiscordException as e:
            await ctx.send(f"오류가 발생했습니다: {str(e)}")

    @slash_command(description="Delete study room and migrate role members")
    @commands.has_permissions(administrator=True)
    async def delete_study(self, ctx, study_name: str, season: str):
        guild = ctx.guild
        season = season.lower()
        year_short = datetime.now().strftime("%y")
        year_long = datetime.now().strftime("%Y")

        role_name = f"{year_short}-{season}-{study_name}"
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            await ctx.send(f"'{role_name}' 역할이 존재하지 않습니다.")
            return

        category = discord.utils.get(guild.categories, name=role_name)
        if category:
            for channel in category.channels:
                if channel.name in [f"{study_name}-채팅", f"{study_name}-음성"]:
                    await channel.delete()

        season_role_name = f"{year_long}_{season}"
        season_role = discord.utils.get(guild.roles, name=season_role_name)
        if not season_role:
            season_role = await guild.create_role(name=season_role_name)

        for member in role.members:
            await member.add_roles(season_role)
            await member.remove_roles(role)

        await role.delete()
        await ctx.send(f"'{role_name}' 스터디 룸과 역할이 삭제되고, 멤버가 '{season_role_name}' 역할로 이동되었습니다.")

def setup(bot):
    bot.add_cog(StudyManager(bot))
    print("StudyManager Cog is loaded")
