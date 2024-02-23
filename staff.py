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

    # Result command
    @commands.slash_command()
    @commands.has_any_role(*management_roles)
    async def result(self, inter, username : disnake.Member, notes : str, result : str = commands.Param(choices=["Accepted", "Denied"])):
        channel = self.client.get_channel(1134394613885575269)
        embed = disnake.Embed(title = "DRPC Application Result", description=inter.author.mention + " **has thoroughly read this application**", color=0xe4d96f)
        if result == "Accepted":
            embed.color = 0x50aa2d
            result_role_id = 1119234205738602537
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1127193899534913668/Application_Results_Green.png?ex=65e3081f&is=65d0931f&hm=321e0563716073b1c4165d878d5681846b150958e4118b441d161c746692870c&=&format=webp&quality=lossless&width=900&height=300")
        
        else:
            embed.color = 0x900000
            result_role_id = 1119234212243984424
            embed.set_image(url="https://media.discordapp.net/attachments/967322688605536278/1127193933684944946/Application_Results_Red.png?ex=65e30828&is=65d09328&hm=151c887209d4daabc6c08c7bb58933f2ac1debfb9d43f819b387f42217585070&=&format=webp&quality=lossless&width=900&height=300")

        guild = inter.guild
        result_role = guild.get_role(result_role_id)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless")
        embed.add_field(name="Result:", value=result_role.mention, inline=False)
        embed.set_author(
        name=f"DRPC Application Readers",
        icon_url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless")
        

        embed.add_field(name="Applicant Username:", value=username.mention, inline=False)    
        embed.add_field(name="Notes:", value=notes, inline=False)
        
        await channel.send(f"{username.mention}")
        await channel.send(embed=embed)
        
        await inter.response.send_message(":white_check_mark: **Sent it to <#1134394613885575269>.**", ephemeral=True)
    
    @result.error
    async def resulterror(self, inter, error):
     if isinstance(error, commands.MissingAnyRole):
      await inter.response.send_message(":x: **Missing permission to run command**", ephemeral = True)
      return
     await inter.response.send_message("Something went really wrong...", ephemeral = True)
     raise error

    # Movement command
    @commands.slash_command()
    @commands.has_any_role(*management_roles)
    async def movement(self, inter, username : disnake.Member, rank : disnake.Role, reason : str, approve = disnake.Member, type : str = commands.Param(choices=["Promotion", "Demotion", "Retirement"])):
        channel = self.client.get_channel(1134061155187433534)
        if type.lower() == "promotion":
            color = 0x50aa2d
            guild = inter.guild
            role = guild.get_role(1120960483357368370)
            image = "https://media.discordapp.net/attachments/967322688605536278/1126981381084426250/Movements_Green.png?ex=65eb7cb3&is=65d907b3&hm=1a95f3251d4ab61511ec1c42ca748b4fc8391ec3b3c1efee5f3de64941bb081c&=&format=webp&quality=lossless&width=900&height=300"

        elif type.lower() ==  "demotion":
            color = 0x900000
            guild = inter.guild
            role = guild.get_role(1120960508275732601)
            image = "https://media.discordapp.net/attachments/967322688605536278/1126981330001997885/Movements_Red.png?ex=65eb7ca7&is=65d907a7&hm=a05305781f55bc5451c8874566ae745a129808cf909886201de63a33f0d0f18e&=&format=webp&quality=lossless&width=900&height=300"
        
        else:
            color = 0x98cfff
            guild = inter.guild
            role = guild.get_role(1125388942007611554)
            image = "https://media.discordapp.net/attachments/967322688605536278/1126981362335879218/Movements_Blue.png?ex=65eb7caf&is=65d907af&hm=ace275d6d915651d9b47ac23437b4e1293bf3b4885c2b61cf7f65ec9ba8cff70&=&format=webp&quality=lossless&width=900&height=300"
            

        embed = disnake.Embed(title = "DRPC Movement", description= "***A staff member's roles have been updated.***", color = color)

        if approve == "":
            approve == inter.author
        
        embed.add_field(name = "Username:", value = username.mention, inline = False)
        embed.add_field(name = "Demotion/Promotion:", value = role.mention, inline = False)
        embed.add_field(name = "Rank:", value = rank.mention, inline = False)
        embed.add_field(name = "Reason:", value = reason, inline = False)
        embed.add_field(name = "Authorised by:", value = approve, inline = False)
        embed.set_image(url=image)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless")
        embed.set_author(
            name=f"DRPC Movements",
            icon_url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless")

        await channel.send(username.mention)
        await channel.send(embed=embed)
        await inter.response.send_message(":white_check_mark: **Sent it to <#1134061155187433534>.**", ephemeral=True)

    @movement.error
    async def resulterror(self, inter, error):
     if isinstance(error, commands.MissingAnyRole):
      await inter.response.send_message(":x: **Missing permission to run command**", ephemeral = True)
      return
     await inter.response.send_message("Something went really wrong...", ephemeral = True)
     raise error
    

    @commands.slash_command()
    @commands.has_any_role(1115611692139819028, 1115635235795775588, 1115636523325460580, 1118966558669164564, 1115611714562555955, 1115695027100864592, 1116311558331580436)
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
