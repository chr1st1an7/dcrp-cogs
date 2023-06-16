import disnake
from disnake.ext import commands
from disnake.ui import SelectMenu, SelectOption

class Staff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Staff Cog is online.')

    @commands.slash_command()
    async def result(self, inter, username: disnake.Member, notes: str):
        options = [
            SelectOption(label='Accepted', value='Accepted'),
            SelectOption(label='Denied', value='Denied')
        ]
        select_menu = SelectMenu(custom_id='result_dropdown', placeholder='Select result', options=options)
        message = await inter.response.send_message(
            'Select the result:',
            view=disnake.ui.View(select_menu)
        )

        def check(interaction: disnake.Interaction):
            return interaction.message == message and interaction.user == inter.author

        try:
            interaction = await self.client.wait_for('select_option', check=check, timeout=60.0)
            result = interaction.data['values'][0]

            embed = disnake.Embed(title='Staff Application Result', color=0xe4d96f)
            if result == 'Accepted':
                embed.color = disnake.Color.green()
                result_role_id = 1119234205738602537
            else:
                embed.color = disnake.Color.red()
                result_role_id = 1119234212243984424

            guild = inter.guild
            result_role = guild.get_role(result_role_id)

            embed.set_author(
                name=f"@{inter.author}",
                icon_url="https://cdn.discordapp.com/attachments/1115898779552456744/1119233504610373672/Namnlos.png"
            )

            embed.add_field(name="Username:", value=username.mention, inline=False)
            embed.add_field(name="Notes", value=notes, inline=False)
            embed.add_field(name="Result:", value=result_role.mention, inline=False)

            channel = self.client.get_channel(1115706650100244580)
            await channel.send(embed=embed)
            await interaction.response.send_message(":white_check_mark: **Sent it to the channel.**", ephemeral=True)

        except TimeoutError:
            await inter.response.send_message(":x: **You took too long to respond. Please try again.**", ephemeral=True)


def setup(client):
    client.add_cog(Staff(client))
