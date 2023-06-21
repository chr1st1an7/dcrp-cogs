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

    
    management_roles = [1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955]

    @commands.slash_command()
    @commands.has_any_role(1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955)
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
    @commands.has_any_role(1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955)
    async def movement(self, inter, username : disnake.Member, rank : disnake.Role, reason : str, approve = disnake.Member, type : str = commands.Param(choices=["Promotion", "Demotion"])):
        channel = self.client.get_channel(1115890559710679081)
        if type.lower() == "promotion":
            color = disnake.Color.green()

        else:
            color = disnake.Color.red()

        embed = disnake.Embed(title = "<:DCRP_LOGO:1120374872950972549> **DCRP Movement** <:DCRP_LOGO:1120374872950972549>", color = color)
        await inter.response.send_message(approve)

    @commands.slash_command()
    @commands.has_any_role(1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955)
    async def partnership(self, inter: disnake.AppCmdInter):
        client = self.client
          # Acknowledge the command before executing

        # Open a modal to get user input
            # Create a modal for text input
        class MyModal(disnake.ui.Modal):
            def __init__(self):
                components = [
                    disnake.ui.TextInput(
                        label="Name",
                        placeholder="DC:RP",
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
                    disnake.ui.TextInput(
                        label="Ping",
                        placeholder="Everyone",
                        custom_id="ping",
                        style=TextInputStyle.short,
                        max_length=50,
                    )
                ]
                super().__init__(title="Partnership Advert", components=components)

            async def callback(self, inter: disnake.ModalInteraction):
                embed = disnake.Embed(title="Partnership Advert")
                for key, value in inter.text_values.items():
                    embed.add_field(
                        name=key.capitalize(),
                        value=value[:1024],
                        inline=False,
                    )

                # ping_value = inter.text_values.get('ping', '').lower()
                # if ping_value == 'everyone':
                #     await inter.send_message(content="@everyone")
                # elif ping_value == 'here':
                #     await inter.send_message(content="@here")

                await inter.edit_original_message(embed=embed)

        modal = MyModal()
        await inter.response.send_modal(modal=modal)


def setup(client):
    client.add_cog(Staff(client))