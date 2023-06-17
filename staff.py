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
    @commands.has_role(1115701058384179300)
    async def partnership(self, inter):
          # Acknowledge the command before executing

    # Open a modal to get user input
        modal = disnake.ui.View()
        modal.input_values = {}  # Dictionary to store input values

        async def callback(interaction):
            for component in interaction.message.components:
                if isinstance(component, disnake.ui.Select):
                    modal.input_values[component.custom_id] = component.values[0]

            #await interaction.response.defer()

        modal.add_item(
            disnake.ui.Select(
                custom_id="input1",
                placeholder="Select an option",
                options=[
                    disnake.SelectOption(label="Option 1", value="option1"),
                    disnake.SelectOption(label="Option 2", value="option2"),
                ]
            )
        )

        modal.add_item(
            disnake.ui.Select(
                custom_id="input2",
                placeholder="Select an option",
                options=[
                    disnake.SelectOption(label="Option A", value="optionA"),
                    disnake.SelectOption(label="Option B", value="optionB"),
                ]
            )
        )

        modal.add_item(disnake.ui.Button(style=disnake.ButtonStyle.primary, label="Submit", custom_id="submit", row=1))
        modal.callback = callback

        await inter.send("Please select options for the embed:", view=modal)

        while len(modal.input_values) < 2:
            await disnake.utils.sleep_until(1)  # Wait for user input

        # Create and send the embed
        embed = disnake.Embed(title="Ping Command", color=disnake.Color.blurple())
        embed.add_field(name="Input 1", value=modal.input_values["input1"])
        embed.add_field(name="Input 2", value=modal.input_values["input2"])
        await inter.send(embed=embed)

def setup(client):
    client.add_cog(Staff(client))