import discord
from discord.commands import slash_command
from discord.ext import commands
from discord.ui import Button, View

from discord_bot.config import GUILD_ID


class ServerManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def excluded_category(name):
        """제외할 카테고리 목록에 포함되는지 확인하는 함수"""
        return name in ["운영진", "멘토", "학교연합", "😄일반", "📞음성 채널", "👥커뮤니티"]

    @slash_command(guild_ids=GUILD_ID, description="Check the category")
    @commands.has_permissions(administrator=True)
    async def show_categories(self, ctx):
        guild = ctx.guild
        view = View(timeout=None)

        for category in guild.categories:
            if not self.excluded_category(category.name):
                button = Button(label=category.name,
                                style=discord.ButtonStyle.primary)

                async def callback(interaction, category=category):
                    role = discord.utils.get(guild.roles, name=category.name)
                    if not role:
                        role = await guild.create_role(name=category.name)

                    if role in interaction.user.roles:
                        await interaction.user.remove_roles(role)
                        await interaction.response.send_message(f"{category.name} 역할이 제거되었습니다.", ephemeral=True)
                    else:
                        await interaction.user.add_roles(role)
                        await interaction.response.send_message(f"{category.name} 역할이 부여되었습니다.", ephemeral=True)

                button.callback = callback
                view.add_item(button)

            await ctx.send("반갑습니다. 구독하고 싶은 카테고리를 선택하세요😉:", view=view)


def setup(bot):
    bot.add_cog(ServerManager(bot))
    print("ServerManager Cog is loaded")
