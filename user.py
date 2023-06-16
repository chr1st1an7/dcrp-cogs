import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction
from disnake.ext import tasks
import random

class User(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'User Cog is online.')

    
    # ------------------------ Commands

    @commands.slash_command()
    async def ping(self, inter):
        latency = round(self.client.latency * 1000)

        await inter.response.send_message(f'Pong! Latency: {latency}ms')

def setup(client):
    client.add_cog(User(client))