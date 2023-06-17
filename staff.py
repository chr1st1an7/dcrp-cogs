import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction
from disnake.ext import tasks
import random
from disnake import TextInputStyle

class Staff(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Staff Cog is online.')

    
    # ------------------------ Commands

    @commands.slash_command()
    @commands.has_role(1115707610247745677)
    async def result(self, inter, username : disnake.Member, notes : str, result : str = commands.Param(choices=["Accepted", "Denied"])):
        channel = self.client.get_channel(1115706650100244580)
        embed = disnake.Embed(title = "Staff Application Result", color=0xe4d96f)
        if result == "Accepted":
            embed.color = disnake.Color.green()
            result_role_id = 1119234205738602537
        
        else:
            embed.color = disnake.Color.red()
            result_role_id = 1119234212243984424

        guild = inter.guild
        result_role = guild.get_role(result_role_id)
        embed.add_field(name="", value=result_role.mention, inline=False)
        embed.set_author(
        name=f"@{inter.author}",
        icon_url="https://cdn.discordapp.com/attachments/1115898779552456744/1119233504610373672/Namnlos.png")
        

        embed.add_field(name="Username:", value=username.mention, inline=False)    
        embed.add_field(name="Notes", value=notes, inline=False)
        
        await channel.send(f"{username.mention}")
        await channel.send(embed=embed)
        
        await inter.response.send_message(":white_check_mark: **Sent it to <#1115706650100244580>.**", ephemeral=True)


    @commands.slash_command()
    @commands.has_any_role(1115701058384179300, 1115635235795775588)
    async def partnership(self, inter: disnake.AppCmdInter):
        client = self.client
          # Acknowledge the command before executing

        # Open a modal to get user input
            # Create a modal for text input
        class MyModal(disnake.ui.Modal):
            def __init__(self):
                # The details of the modal, and its components
                components = [
                    disnake.ui.TextInput(
                        label="Name",
                        placeholder="Foo Tag",
                        custom_id="name",
                        style=TextInputStyle.short,
                        max_length=50,
                    ),
                    disnake.ui.TextInput(
                        label="Description",
                        placeholder="Lorem ipsum dolor sit amet.",
                        custom_id="description",
                        style=TextInputStyle.paragraph,
                    ),
                ]
                super().__init__(title="Create Tag", components=components)

            # The callback received when the user input is completed.
            async def callback(self, inter: disnake.ModalInteraction):
                embed = disnake.Embed(title="Tag Creation")
                for key, value in inter.text_values.items():
                    embed.add_field(
                        name=key.capitalize(),
                        value=value[:1024],
                        inline=False,
                    )
                await inter.response.send_message(embed=embed)


def setup(client):
    client.add_cog(Staff(client))