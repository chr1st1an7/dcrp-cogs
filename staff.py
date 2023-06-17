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
    @commands.has_any_role(1115701058384179300, 1115635235795775588)
    async def partnership(self, inter, ping : str = commands.Param(choices=["No", "Here", "Everyone"])):
        client = self.client
          # Acknowledge the command before executing

        # Open a modal to get user input
            # Create a modal for text input
        class InputModal(disnake.ui.View):
            def __init__(self):
                super().__init__()
                self.input_value = None

            @disnake.ui.button(label="Cancel", style=disnake.ButtonStyle.danger)
            async def cancel(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                self.input_value = None
                await interaction.message.edit(view=None)

            @disnake.ui.button(label="Submit", style=disnake.ButtonStyle.primary)
            async def submit(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                await interaction.message.edit(view=None)

        modal = InputModal()

        # Prompt the user for input
        await inter.send("Please enter the advert:")

        # Wait for user input
        response = await client.wait_for("message", check=lambda m: m.author.id == inter.user.id)

        # Store the input value
        modal.input_value = response.content

        # Create and send the embed
        embed = disnake.Embed(title="Partnership Advert", description=modal.input_value, color=disnake.Color.blurple())
        disnake.AllowedMentions(mention_here=True)
        disnake.AllowedMentions(mention_everyone=True)
        if ping.lower == "no":
            pass
        
        elif ping.lower == "here":
            await inter.send("@here")

        else:
            await inter.send("@everyone")
        await inter.send(embed=embed, view=modal)

def setup(client):
    client.add_cog(Staff(client))