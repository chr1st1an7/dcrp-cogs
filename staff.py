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
    async def result(self, inter, username : disnake.Member, reason : str, result : str = commands.Param(choices=["Accepted", "Denied"])):
        embed = disnake.Embed(title = "Staff Application Results", description = "Here are the results for your application, thanks your applying!", color=0xe4d96f)
        embed.add_field(name="Username:", value=username.mention)
        embed.add_field(name="Result:", value=result)
        embed.add_field(name="Reason", value=reason)
        if result == "Accepted":
            embed.set_thumbnail(url="https://discord.com/assets/212e30e47232be03033a87dc58edaa95.svg")
        else:
            embed.set_thumbnail(url="https://discord.com/assets/8becd37ab9d13cdfe37c08c496a9def3.svg")
        await inter.response.send_message(embed=embed)

def setup(client):
    client.add_cog(Staff(client))