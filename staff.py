import disnake
from disnake.ext import commands
from disnake.ext.commands import command, has_permissions, bot_has_permissions, BucketType
from datetime import datetime
import time

class Staff(commands.Cog):
    client = commands
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Staff Cog is online.')


    management_roles = [1115611692139819028, 1116311558331580436, 1115633196336422942, 1122489752579485796]
    
    # Result command
    @commands.slash_command()
    @commands.cooldown(rate=1, per=20, type=BucketType.member)
    @commands.has_any_role(*management_roles)
    async def result(self, inter, username : disnake.Member, notes : str, result : str = commands.Param(choices=["Accepted", "Denied"])):
        await inter.response.defer(ephemeral=True)
        channel = self.client.get_channel(1134394613885575269)
        embed = disnake.Embed(title = "DRPC Application Result", description=f"{inter.author.mention}**has thoroughly read this application**", color=0xe4d96f)
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
        await channel.send(f"{username.mention}", embed=embed)
        await inter.followup.send(":white_check_mark: **Sent it to <#1134394613885575269>.**", delete_after=(5), ephemeral=True)

    @result.error
    async def resulterror(self, inter, error):
     if isinstance(error, commands.MissingAnyRole):
      await inter.response.send_message(":x: **Missing permission to run command**", delete_after=(5), ephemeral = True)
      return
     await inter.response.send_message("Something went really wrong...", delete_after=(5), ephemeral = True)
     raise error

    # Movement command
    @commands.slash_command()
    @commands.has_any_role(*management_roles)
    async def movement(self, inter, username : disnake.Member, rank : disnake.Role, reason : str, approve = disnake.Member, type : str = commands.Param(choices=["Promotion", "Demotion", "Retirement"])):
        await inter.response.defer(ephemeral=True)
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
        await channel.send(f"{username.mention}", embed=embed)
        await inter.followup.send(":white_check_mark: **Sent it to <#1134061155187433534>.**", delete_after=(5), ephemeral=True)

    @movement.error
    async def resulterror(self, inter, error):
     if isinstance(error, commands.MissingAnyRole):
      await inter.response.send_message(":x: **Missing permission to run command**", delete_after=(5), ephemeral = True)
      return
     await inter.response.send_message("Something went really wrong...", delete_after=(5), ephemeral = True)
     raise error


    @commands.slash_command()
    @commands.has_any_role(1145668152018092142)
    async def ra(self, inter, username : disnake.Member, roblox_username : str, time : str, ping : disnake.Member, number : str = commands.Param(choices=["1st R/A", "2nd R/A"])):
        await inter.response.defer(ephemeral=True)
        channel = self.client.get_channel(1134066792889860167)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        embed = disnake.Embed(title = " **DCRP Ridealong Request** ", color=0x827abd, description = "***A staff member has requested a ridealong***")

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
        embed.set_footer(text = f"Time of Request: @ {current_time}")

        await channel.send(f"{ping.mention}", embed=embed)
        await inter.followup.send(":white_check_mark: **Sent it to <#1134066792889860167>.**", delete_after=(5), ephemeral=True)

    @ra.error
    async def resulterror(self, inter, error):
     if isinstance(error, commands.MissingAnyRole):
      await inter.response.send_message(":x: **You must have the <@&1145668152018092142> role to run this command.**", delete_after=(5), ephemeral = True)
      return
     await inter.response.send_message("Something went really wrong...", delete_after=(5), ephemeral = True)
     raise error   

    @commands.slash_command()
    @commands.has_any_role(1115703473988702368) 
    async def session(self, inter):
       await inter.response.defer(ephemeral=True)
       epochtime = int(time.time())
       channel_id = 1134051764568596540
       channel = self.client.get_channel(channel_id)
       except_message = await channel.fetch_message(1205554906983956572)

       bot_messages = await channel.history(limit=None).filter(lambda msg: msg.author == self.client.user).flatten()
       mentioned_everyone = any("@everyone" in msg.content for msg in bot_messages)
       await channel.purge(check=lambda msg: msg.id != except_message.id)

       if mentioned_everyone:
        Title = "Dallas Roleplay Server Shutdown"
        Image = "https://media.discordapp.net/attachments/967353279552053292/1126803993344090192/Server-Shutdown.png?ex=65ead77f&is=65d8627f&hm=3e847960769d9aaecd5d83129001be8d8c5a6b956abec9fbb7ff1f57cdda8f3a&=&format=webp&quality=lossless&width=900&height=300"
        Footer = "We'll see you in the next SSU!"
        Desc = ('The Dallas County Roleplay server is currently **shutdown**. At this time we recommend you to not join the server as it is not going to be moderated.\n\n**SSU Times:**\n<t:1707066000:t> - Weekdays\n<t:1707062400:t> - Saturdays\n<t:1707058800:t> - Sundays\n\n*Please note that these times are an estimate and we may occasionally hold SSUs at any time that we find fit.*\n\n**Since:** <t:{0}:f>\n**Author:** {1}'.format(epochtime, inter.author.mention))  
       else:
        Title = "Dallas Roleplay Server Startup"
        Image = "https://cdn.discordapp.com/attachments/967353279552053292/1126803975677685812/Server-Startup.png"
        Footer = "Join the best Dallas roleplay experience right now!"
        Desc = ("**Dallas Roleplay Community | Strict**\nCode: **dallasRP**\n**Invite link:** [here](https://policeroleplay.community/join/dallasRP)\n\n**Since:** <t:{0}:f>\n**Author:** {1}".format(epochtime, inter.author.mention))

       embed = disnake.Embed(title=Title, description=Desc, color=0x827abd)
       embed.set_author(
          name="Dallas Roleplay Sessions", 
          icon_url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless"
       )
       embed.set_footer(text=Footer)
       embed.set_image(url=Image)
       embed.set_thumbnail(url="https://media.discordapp.net/attachments/1134066455932051538/1206575134350245919/Untitled.png?ex=65e5bc29&is=65d34729&hm=9be3e9cd9ba51b446099746b408863040666013ec5c41c3272e1a896124d3b39&=&format=webp&quality=lossless&width=900&height=671")
       if mentioned_everyone:
          await channel.send(embed=embed)
       else:
          await channel.send("@everyone", embed=embed)
       await inter.followup.send("Sent", ephemeral=True)


    @session.error
    async def resulterror(self, inter, error):
     if isinstance(error, commands.MissingAnyRole):
      await inter.response.send_message(":x: **You must have the <@&1115703473988702368> role to run this command.**", delete_after=(5), ephemeral = True)
      return
     await inter.response.send_message("Something went really wrong...", delete_after=(5), ephemeral = True)
     raise error

def setup(client):
    client.add_cog(Staff(client))