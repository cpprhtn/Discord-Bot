import discord
from discord.ext import commands
from discord_bot.config import GUILD_ID
from discord.commands import slash_command
from discord.ui import Button, View

class CategoryManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @slash_command(guild_ids=GUILD_ID, description="Display the category list")
    @commands.has_permissions(administrator=True)
    async def display_category_list(self, interaction):
        guild = interaction.guild
        embed = discord.Embed(title="카테고리 목록", color=discord.Color.blue())
        for category in guild.categories:
            embed.add_field(name=category.name, value=f"카테고리 ID: {category.id}", inline=False)
        await interaction.response.send_message(embed=embed)

    @slash_command(guild_ids=GUILD_ID, description="Create a category and role")
    @commands.has_permissions(administrator=True)
    async def create_category(self, interaction, name: str):
        guild = interaction.guild
        upper_name = name.upper()

        role = discord.utils.get(guild.roles, name=upper_name)
        if not role:
            role = await guild.create_role(name=upper_name)
            await interaction.response.send_message(f"'{upper_name}' 역할이 생성되었습니다.", ephemeral=True)
        else:
            await interaction.response.send_message(f"'{upper_name}' 역할이 이미 존재합니다.", ephemeral=True)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            role: discord.PermissionOverwrite(view_channel=True)
        }
        category = await guild.create_category(name=upper_name, overwrites=overwrites)
        await interaction.followup.send(f"'{upper_name}' 카테고리와 역할이 생성되었습니다.")

    @slash_command(guild_ids=GUILD_ID, description="Delete a category and role")
    @commands.has_permissions(administrator=True)
    async def delete_category(self, interaction, category_name: str):
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name=category_name)
        
        if category is None:
            await interaction.response.send_message(f"'{category_name}' 카테고리가 존재하지 않습니다.", ephemeral=True)
            return
        
        await category.delete()
        await interaction.response.send_message(f"'{category_name}' 카테고리가 삭제되었습니다.", ephemeral=True)

        role = discord.utils.get(guild.roles, name=category_name.upper())
        if role is not None:
            await role.delete()
            await interaction.followup.send(f"'{category_name}' 역할이 삭제되었습니다.")

def setup(bot):
    bot.add_cog(CategoryManager(bot))
    print("CategoryManager Cog is loaded")
