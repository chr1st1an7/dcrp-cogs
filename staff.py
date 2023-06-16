import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction
from disnake.ext import tasks
import random

class Staff(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Staff Cog is online.')

    
    # ------------------------ Commands

    @commands.slash_command()
    async def result(self, inter, username : disnake.Member, notes : str, result : str = commands.Param(choices=["Accepted", "Denied"])):
        embed = disnake.Embed(title = "Staff Application Results", color=0xe4d96f)
        
        embed.set_author(
        name=f"@{inter.author}",
        icon_url="https://cdn.discordapp.com/attachments/1115898779552456744/1119233504610373672/Namnlos.png")
        if result == "Accepted":
            embed.color = disnake.Color.green()
            result = 1119234205738602537
        
        else:
            embed.color = disnake.Color.red()
            result = 1119234212243984424

        embed.add_field(name="Username:", value=username.mention, inline=False)    
        embed.add_field(name="Notes", value=notes, inline=False)
        embed.add_field(name="Result:", value=result.mention, inline=False)
        await inter.response.send_message(embed=embed)

def setup(client):
    client.add_cog(Staff(client))