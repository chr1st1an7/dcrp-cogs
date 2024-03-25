import disnake
from disnake.ext import commands

class MyModal(disnake.ui.Modal):
    def __init__(self, drop_down_view):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Product:",
                placeholder="Uniform, Livery, etc",
                custom_id="name",
                style=disnake.TextInputStyle.short,
                max_length=50,
                required=True
            ),
            disnake.ui.TextInput(
                label="Review:",
                placeholder="Lorem ipsum dolor sit amet.",
                custom_id="description",
                style=disnake.TextInputStyle.paragraph,
                required=True
            ),
        ]
        super().__init__(title="Create Review", components=components)
        self.drop_down_view = drop_down_view

    # The callback received when the user input is completed.
    async def callback(self, inter: disnake.ModalInteraction):
        self.drop_down_view.submit_callback.disabled = False
        self.drop_down_view.Note_callback.label = "Edit Note"
        await DropDownView.callback(self.drop_down_view, inter)  # Pass the instance of DropDownView

        

class DropDownView(disnake.ui.View):
    message: disnake.Message

    def __init__(self, options):
        super().__init__(timeout=180.0)
        self.rating = None
        self.user = None
        self.values = None
        self.designer_callback.options = options
        rating = []
        self.emojis = {
            1: "⭐",
            2: "⭐⭐",
            3: "⭐⭐⭐",
            4: "⭐⭐⭐⭐",
            5: "⭐⭐⭐⭐⭐"
        }
        for number in range(1, 6):
            rating.append(disnake.SelectOption(label=self.emojis.get(number, ""), value=number))
        self.rating_callback.options = rating
    
    @disnake.ui.string_select(placeholder="Select a designer", min_values=1, max_values=1)
    async def designer_callback(self, select: disnake.ui.StringSelect, inter: disnake.MessageInteraction):
        self.user = select.values[0]
        for option in self.designer_callback.options:
            if int(self.user) == int(option.value):
                option.default = True
                print("true", option.value, self.user)
            else:
                option.default = False
                print("false", option.value, self.user)
        if self.user is not None:
            self.rating_callback.disabled = False
            await inter.response.edit_message(view=self)
        else: 
            await inter.response.defer(with_message=False)

   
    @disnake.ui.string_select(placeholder="Select a rating", min_values=1, max_values=1, disabled=True)                
    async def rating_callback(self, select: disnake.ui.StringSelect, inter: disnake.MessageInteraction):
        self.rating = select.values[0]
        for option in self.rating_callback.options:
            if int(self.rating) == int(option.value):
                option.default = True
                print("true", option.value, self.rating)
            else:
                option.default = False
                print("false", option.value, self.rating)
        if self.user is not None and self.rating is not None:
            self.Note_callback.disabled = False
            await inter.response.edit_message(view=self)
        else: 
            await inter.response.defer(with_message=False)

    
    @disnake.ui.button(label="Submit", style=disnake.ButtonStyle.green, disabled=True)
    async def submit_callback(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):    
        embed1 = disnake.Embed(color=0x4332A2)
        embed1.set_image(url="https://media.discordapp.net/attachments/1151424906123284510/1220105563623522387/22222.png?ex=660dbada&is=65fb45da&hm=8d18b04cfa9c0b54582d5f2870a6ef6cb0197003f4000cda5ca9aed38015792f&=&format=webp&quality=lossless&width=900&height=338")
        embed2 = disnake.Embed(title="Dallas Designs™ Customer Review", color=0x4332A2)
        embed2.set_image(url="https://media.discordapp.net/attachments/1151424906123284510/1220107658443493396/44444.png?ex=660dbcce&is=65fb47ce&hm=2d406a48918ffb3cb8a14f44d8e55ac4b5fa510b6b7dd6f5183aa9a53f47df97&=&format=webp&quality=lossless&width=900&height=113")
        embed2.set_author(name=f'Reviewed by {inter.author.name}', icon_url=inter.author.avatar)
        embed2.add_field(name='<:dot_dot:1221919201116160011>Designer:', value=f'<:arrow_arrow:1221914053631410226><@{self.user}>', inline=True)
        embed2.add_field(name='<:dot_dot:1221919201116160011>Product:', value=f"<:arrow_arrow:1221914053631410226>{self.values[0]}", inline=True)
        embed2.add_field(name='<:dot_dot:1221919201116160011>Comments:', value=f"<:arrow_arrow:1221914053631410226>{self.values[1]}", inline=False)
        embed2.add_field(name="<:dot_dot:1221919201116160011>Overall rating:", value=f"<:arrow_arrow:1221914053631410226>{self.emojis.get(int(self.rating))}")
        await inter.response.edit_message("Sent!", view=None)
        await inter.channel.send(view=None, embeds=[embed1, embed2])
    
    @disnake.ui.button(label="Add Note", style=disnake.ButtonStyle.blurple, disabled=True)
    async def Note_callback(self, button: disnake.ui.Button, inter: disnake.MessageInteraction):    
        await inter.response.send_modal(MyModal(self))

    @staticmethod
    async def callback(self, inter):
        self.values = []
        for key, value in inter.text_values.items():
            self.values.append(value)
        await inter.response.edit_message(view=self)


class Designs(commands.Cog):  
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Dallas Designs Cog is online.')

    @commands.slash_command()
    async def review(self, inter: disnake.ApplicationCommandInteraction):
        options = []
        for member in inter.guild.members:
            emoji_names = [emoji.name for emoji in inter.guild.emojis]
            if member.get_role(1115637257244790854) and member.id != inter.author.id:
                if f'{member.id}' not in emoji_names:
                  await inter.guild.create_custom_emoji(name=f'{member.id}', image=await member.avatar.replace(size=128, format='png').read())
                for emoji in inter.guild.emojis:
                  if emoji.name == f'{member.id}':
                    Avatar = emoji
                options.append(disnake.SelectOption(label=member.display_name, value=member.id, emoji=Avatar))
            elif not member.get_role(1115637257244790854):
                for emoji in inter.guild.emojis:
                  if emoji.name == f'{member.id}':
                    await emoji.delete()
        
        view = DropDownView(options=options)
        await inter.response.send_message(view=view, ephemeral=True)



def setup(bot):
    bot.add_cog(Designs(bot))
