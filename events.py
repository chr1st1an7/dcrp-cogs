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
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1210987536554532924)
        embed = {
          'footer': {'text': 'Questions? Do not hesitate to ask our staff members!'},
          'image': {
          'url': 'https://media.discordapp.net/attachments/967353279552053292/1126841923710234724/ezgif.com-gif-maker_1.gif?width=900&height=300&ex=65f43552&is=65e1c052&hm=6acf5d7b4e9ccb2f7b93ec34f9b18c0a56162456a1d4dfa1cbc36372111a638b&',
        },
          'thumbnail': {
          'url': 'https://media.discordapp.net/attachments/1134066455932051538/1206575134350245919/Untitled.png?ex=65eef6a9&is=65dc81a9&hm=4f32dee80cd868edee4de1ada54ce42e0a5313f66ab396782edfd4fc6201278b&=&format=webp&quality=lossless&width=900&height=671',
        },
          'author': {
          'name': 'Dallas Roleplay',
          'icon_url': 'https://media.discordapp.net/attachments/1134066455932051538/1206575134350245919/Untitled.png?ex=65eef6a9&is=65dc81a9&hm=4f32dee80cd868edee4de1ada54ce42e0a5313f66ab396782edfd4fc6201278b&=&format=webp&quality=lossless&width=900&height=671',
        },
          'color': 8551101,
          'type': 'rich',
          'description': f'*to the cityscapes of* ***Texas,*** *{member.mention}! We now have* ***{member.guild.member_count}*** *members.* \n\n*Make sure to read our rules*. *They can be found in* ***<#1134046508753375244>*** *and* ***<#1134038859731189831>***\n\nThe **[Staff Application](https://forms.gle/uYCmAyDtCxQ1iiGX9)** or **[Ban Appeal](https://forms.gle/cMJCBiBnwmQT1gRH8)** can be found in **<#1134047342262243430>**, as well as in <#1134049666741309495>.',
          'title': 'Welcome!'
        }
        self.mention = member.mention
        await channel.send(member.mention, embed=disnake.Embed.from_dict(embed))
        
    @commands.Cog.listener()
    async def on_message(self, message):
        # Application autoresponse
        if message.author == self.bot.user:
            return
        if re.search(r'\b(apply|application)\b', message.content.lower()):
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
        
        # Do not ping Founders/Presidential autoresponse
        mentions = message.raw_mentions
        exists = any(id in [495517683429801984, 649280874550132746, 474938992966631425, 957733978666840085] for id in mentions)
        if message.author == self.bot.user:
            return
        if exists and message.author.get_role(1115695027100864592) is None and message.author.get_role(1144303846647156837) is None and message.author.get_role(1115642951272505405) is None: 
            embed = disnake.Embed(color=0x827abd, description="Please do not ping <@&1122489752579485796>. They are often busy and have very limited time. If you need any support then please contact <@&1116311558331580436> instead. Alternatively, you may also open a ticket in <#1134082915123335282>." )
            embed.set_author(name="DRPC Ownership", icon_url="https://media.discordapp.net/attachments/1134066455932051538/1206575134350245919/Untitled.png?ex=65e5bc29&is=65d34729&hm=9be3e9cd9ba51b446099746b408863040666013ec5c41c3272e1a896124d3b39&=&format=webp&quality=lossless&width=900&height=671")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1134066455932051538/1206575134350245919/Untitled.png?ex=65e5bc29&is=65d34729&hm=9be3e9cd9ba51b446099746b408863040666013ec5c41c3272e1a896124d3b39&=&format=webp&quality=lossless&width=900&height=671")
            await message.reply(embed=embed) 


def setup(bot):
    bot.add_cog(Events(bot))
