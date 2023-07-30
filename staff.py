import disnake
from disnake import message
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions
from disnake.ui import View, Button, button
from disnake import ButtonStyle, Interaction
from disnake.ext import tasks
import random
from disnake import TextInputStyle
import datetime

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
        channel = self.client.get_channel(1134394613885575269)
        embed = disnake.Embed(title = "DCRP Application Result", color=0xe4d96f, description=f"***{inter.author.mention} has thoroughly read this application.*** ")
        embed.set_author(name = "DCRP Application Readers", icon_url="https://media.discordapp.net/attachments/1115898779552456744/1120345364780810410/DCRP_LOGO.png")
        if result == "Accepted":
            embed.color = 0x50aa2d
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1127193899534913668/Application_Results_Green.png?width=900&height=300")
            result_role_id = 1119234205738602537
        
        else:
            embed.color = 0x900000
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1127193933684944946/Application_Results_Red.png?width=900&height=300")
            result_role_id = 1119234212243984424

        guild = inter.guild
        result_role = guild.get_role(result_role_id)
        embed.add_field(name="", value=result_role.mention, inline=False)
        embed.set_author(
        name=f"@{inter.author}",
        icon_url="https://cdn.discordapp.com/attachments/1115898779552456744/1119233504610373672/Namnlos.png")
        
        embed.add_field(name="**Result:**", value=result.mention, inline=False)    
        embed.add_field(name="**Application Username:**", value=username.mention, inline=False)    
        embed.add_field(name="**Notes**", value=notes, inline=False)

        
        
        await channel.send(f"{username.mention}")
        await channel.send(embed=embed)
        
        


    @commands.slash_command()
    @commands.has_any_role(1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955, 1116311558331580436, 1115633196336422942)
    async def movement(self, inter, username : disnake.Member, rank : disnake.Role, reason : str, approve = disnake.Member, type : str = commands.Param(choices=["Promotion", "Demotion", "Retirement"])):
        embed = disnake.Embed(title = "**DCRP Movement**", description="*** A staff member's roles have been updated. ***")
        
        if type.lower() == "promotion":
            color = 0x50aa2d
            guild = inter.guild
            role = guild.get_role(1120960483357368370)
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1126981381084426250/Movements_Green.png?width=900&height=300")

        elif type.lower() ==  "demotion":
            color = 0x900000
            guild = inter.guild
            role = guild.get_role(1120960508275732601)
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1126981330001997885/Movements_Red.png?width=900&height=300")
        
        else:
            color = 0x98cfff
            guild = inter.guild
            role = guild.get_role(1125388942007611554)
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1126981362335879218/Movements_Blue.png?width=900&height=300")
        
        embed.color = color
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        channel = self.client.get_channel(1134061155187433534)
        

       


        if approve == "":
            approve == inter.author
        
        embed.set_author(name = "DCRP Movements", icon_url="https://media.discordapp.net/attachments/1115898779552456744/1120345364780810410/DCRP_LOGO.png")
        embed.add_field(name = "Username:", value = username.mention, inline = False)
        embed.add_field(name = "Movement Type:", value = role.mention, inline = False)
        embed.add_field(name = "New Rank:", value = rank.mention, inline = False)
        embed.add_field(name = "Reason:", value = reason, inline = False)
        embed.add_field(name = "Authorised by:", value = approve, inline = False)
        

        embed.set_footer(text = f"Time of Movement: • {current_time}")

        await channel.send(username.mention)
        await channel.send(embed=embed)
        await inter.response.send_message(":white_check_mark: **Sent it to <#1134061155187433534>.**", ephemeral=True)

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

    @commands.slash_command()
    @commands.has_any_role(1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955, 1115695027100864592)
    async def ra(self, inter, username : disnake.Member, roblox_username : str, time : str, ping : disnake.Member, number : str = commands.Param(choices=["1st R/A", "2nd R/A"])):
        channel = self.client.get_channel(1134066792889860167)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        

        color = 0x827abd
        embed = disnake.Embed(title = " **DCRP Ridealong Request** ", color = color, description = "***A staff member has requested a ridealong***")

        embed.set_author(name = "DCRP Ridealongs", icon_url="https://media.discordapp.net/attachments/1115898779552456744/1120345364780810410/DCRP_LOGO.png")
        embed.add_field(name = "Discord username:", value = username.mention, inline = False)
        embed.add_field(name = "Roblox username:", value = roblox_username, inline = False)
        embed.add_field(name = "Time:", value = time, inline = False)
        embed.add_field(name = "Ping:", value = ping.mention, inline = False)

        if number.lower() == "1st r/a":
            embed.add_field(name = "Ridealong number", value = "1st R/A", inline = False)

        if number.lower() ==  "2nd r/a":
            embed.add_field(name = "Ridealong number", value = "2nd R/A", inline = False)

        embed.set_image(url = "https://cdn.discordapp.com/attachments/967322688605536278/1127164653240328222/Ridealongs.png")
        embed.set_footer(text = f"Time of Request: • {current_time}")

        await channel.send(ping.mention)
        await channel.send(embed=embed) #827abd
       
        await inter.response.send_message(":white_check_mark: **Sent it to <#1134066792889860167>.**", ephemeral=True)

def setup(client):
    client.add_cog(Staff(client))