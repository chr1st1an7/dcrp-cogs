import disnake
from disnake.ext import commands
from disnake.ui import View, Button, Select

class ResultModal(disnake.ui.View):
    def __init__(self, inter, username, notes):
        super().__init__()
        self.inter = inter
        self.username = username
        self.notes = notes
        
        self.result = None  # Variable to store the selected result
    
    async def callback(self, interaction: disnake.Interaction):
        if interaction.component.id == 'result_dropdown':
            self.result = interaction.data['values'][0]
    
    @disnake.ui.button(label='Submit', style=disnake.ButtonStyle.primary)
    async def submit_button(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if self.result is None:
            await interaction.response.send_message('Please select a result.', ephemeral=True)
            return
        
        channel = self.inter.channel
        embed = disnake.Embed(title='Staff Application Result', color=0xe4d96f)
        
        if self.result == 'Accepted':
            embed.color = disnake.Color.green()
            result_role_id = 1119234205738602537
        else:
            embed.color = disnake.Color.red()
            result_role_id = 1119234212243984424
        
        guild = self.inter.guild
        result_role = guild.get_role(result_role_id)
        
        embed.set_author(
            name=f"@{self.inter.author}",
            icon_url="https://cdn.discordapp.com/attachments/1115898779552456744/1119233504610373672/Namnlos.png"
        )
        
        embed.add_field(name="Username:", value=self.username.mention, inline=False)
        embed.add_field(name="Notes", value=self.notes, inline=False)
        embed.add_field(name="Result:", value=result_role.mention, inline=False)
        
        await channel.send(embed=embed)
        await interaction.response.send_message(":white_check_mark: **Sent it to the channel.**", ephemeral=True)


class Staff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Staff Cog is online.')

    @commands.slash_command()
    async def result(self, inter, username: disnake.Member, notes: str):
        modal_view = ResultModal(inter, username, notes)
        select = Select(
            placeholder='Select result',
            options=[
                disnake.SelectOption(label='Accepted', value='Accepted'),
                disnake.SelectOption(label='Denied', value='Denied')
            ],
            custom_id='result_dropdown',
            max_values=1,
            min_values=1
        )
        modal_view.add_item(select)
        await inter.response.send_message('Select the result:', view=modal_view)


def setup(client):
    client.add_cog(Staff(client))
