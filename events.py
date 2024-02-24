import disnake
from disnake.ext import commands
import re

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Events Cog is online.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if re.search(r'\b(apply|application)\b' , message.content.lower()):
            if message.author.get_role(1115695027100864592) is None:
             embed = disnake.Embed(
                title="Staff Application", 
                description='The staff application can be found if you head to <#1134049666741309495> and find the staff application section or <#1134047342262243430> and find "How to become staff".',
                color = 0x827abd
                )
             embed.set_author(
                name=f"Dallas Roleplay Community Applications",
                icon_url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless"
                )
             embed.set_footer(text="If you have any more questions, don't hesitate to ask our staff members!")
             embed.add_field(name="Department Applications", value='Department applications can be found in their respective Discord servers. Invite links to these server can be found in <#1134054261974646815>.  Please note that you can only apply to one department.')
             embed.set_image(url="https://media.discordapp.net/attachments/1134066455932051538/1148195104021024820/Applications_Staff.png?ex=65e59b05&is=65d32605&hm=c6c10772d51b4578958fc63e6d98d6e8918d212ffadd330c0815e02cef5daa45&=&format=webp&quality=lossless&width=900&height=300")
             embed.set_thumbnail(url="https://media.discordapp.net/attachments/1134066455932051538/1205550344331985006/ggdrpc-removebg-preview.png?ex=65eb3c40&is=65d8c740&hm=ea84f8b9c9c6ad0077f14da769ccbf1adbe7eac5215a9fb7b9b0953e586aeff5&=&format=webp&quality=lossless")
             await message.reply(embed=embed)

    
        

def setup(bot):
    bot.add_cog(Events(bot))
