import disnake
from disnake import emoji
from disnake.ext import commands
import asyncio
import time

discord_logo = "<:Discord:1212332474709975111> "
game_logo = "<:Roblox:1212332477318823946>"
tickets_logo = "<:ticket_:1212110002630950922>"
question_mark = "<:Question_Mark_Purple:1212335978627334206>"
home_purple = "<:Home_Purple:1212853739178958939>"
information_purple = "<:Information_Purple:1213159021905977385>"
cross = "<:White_Cross:1212140437666795531>"
left_arrow = "<:left_arrow_white:1213063724743786506>"
flag_purple = "<:flag_purple:1213069865221361684>"
bot_purple = "<:bot_purple:1213159017757544449>"

class Help(commands.Cog):
      client = commands
      def __init__(self, client):
        self.client = client
        self.slash_command_interactions = {}
        self.timers = {}

      @commands.Cog.listener()
      async def on_ready(self):
       print(f'Help Cog is online.')


      async def timer(self, inter, message):
       await asyncio.sleep(30)
       await message.delete()

      async def NewMenu(self, inter, menu, message):
        if menu == "main":
          embed = disnake.Embed(title="DRPC Help Panel", description="What do you need help with?", color=0x827abd)
          new_components = [
                  disnake.ui.Button(label="Server", style=disnake.ButtonStyle.grey, emoji = home_purple, custom_id="Server"),
                  disnake.ui.Button(label="Bot", style=disnake.ButtonStyle.grey, emoji = bot_purple, custom_id="Bot"),
                  disnake.ui.Button(label="Close", style=disnake.ButtonStyle.blurple, emoji = cross, custom_id="Close"),
          ]
          try:
            await inter.response.edit_message(components=new_components, embed=embed)
          except:
            await inter.followup.send(components=new_components, embed=embed)
            message = await inter.original_response()
            self.timers[message.id] = asyncio.create_task(self.timer(inter, message))
        elif menu == "server":
          embed = disnake.Embed(title="DRPC Server Help Panel", description='For information on the server, press **"Info"**. \nFor Human Help, press **"Support"**.', color=0x827abd)
          new_components = [
              disnake.ui.Button(label="Info", style=disnake.ButtonStyle.grey, emoji = information_purple, custom_id="Server_Info"),
              disnake.ui.Button(label="Support", style=disnake.ButtonStyle.url, url = "https://discord.com/channels/1115610852373049354/1134082915123335282", emoji = tickets_logo),
              disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji = left_arrow, custom_id="Back")
          ]
          await inter.response.edit_message(components=new_components, embed=embed)
        elif menu == "server_info":
          embed = disnake.Embed(title="DRPC Server Information Panel", description="Here you find Discord Rules, Game rules, FAQ and role information.", color=0x827abd)
          new_components = [
              disnake.ui.Button(label="Rules", style=disnake.ButtonStyle.grey, emoji = discord_logo, custom_id="Discord_Rules"),
              disnake.ui.Button(label="Rules", style=disnake.ButtonStyle.grey, emoji = game_logo, custom_id="Game_Rules"),
              disnake.ui.Button(label="FAQ", style=disnake.ButtonStyle.url, url = "https://discord.com/channels/1115610852373049354/1134047342262243430", emoji = question_mark),
              disnake.ui.Button(label="Roles", style=disnake.ButtonStyle.url, url = "https://discord.com/channels/1115610852373049354/1134067567334539304", emoji = flag_purple),
              disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji = left_arrow, custom_id="Server")
          ]
          await inter.response.edit_message(components=new_components, embed=embed)
        elif menu == "bot":
          embed = disnake.Embed(title="DRPC Bot Information Panel", description="To be done", color=0x827abd)
          new_components = [
              disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji = left_arrow, custom_id="Back")
          ]
          await inter.response.edit_message(components=new_components, embed=embed)

      @commands.slash_command()
      async def help(self, inter: disnake.ApplicationCommandInteraction): 
        await inter.response.defer()
        await self.NewMenu(inter, "main", None)


      @commands.Cog.listener()
      async def on_button_click(self, inter: disnake.Interaction):
       if inter.component.custom_id not in ["Discord_Rules", "Game_Rules", "Server", "Back", "Server_Info", "Close", "Bot"]:
          return
       if inter.author.id != inter.message.interaction.author.id:
          await inter.response.send_message("This is not your interaction", delete_after=(5), ephemeral=True)
          return

       if inter.component.custom_id == "Server":
        await self.NewMenu(inter, "server", None)
       if inter.component.custom_id == "Bot":
         await self.NewMenu(inter, "bot", None)
       if inter.component.custom_id == "Back":
         await self.NewMenu(inter, "main", None)
       if inter.component.custom_id == "Server_Info":
         await self.NewMenu(inter, "server_info", None)
       if inter.component.custom_id == "Close":
         await inter.message.delete()
         self.timers[inter.message.id].cancel()
       if inter.component.custom_id == "Discord_Rules":
         await inter.response.defer(with_message=True, ephemeral=True)
         channel = self.client.get_channel(1134038859731189831)
         Rules = await channel.fetch_message(1205550773455294566)
         embeds = Rules.embeds
         await inter.followup.send(embeds=embeds, ephemeral=True)
       if inter.component.custom_id == "Game_Rules":
         await inter.response.defer(with_message=True, ephemeral=True)
         channel = self.client.get_channel(1134046508753375244)
         Rules = await channel.fetch_message(1205554518335553536)
         embeds = Rules.embeds
         await inter.followup.send(embeds=embeds, ephemeral=True)

       if inter.message.id in self.timers:
            self.timers[inter.message.id].cancel()
       self.timers[inter.message.id] = asyncio.create_task(self.timer(inter, inter.message))

def setup(bot):
    bot.add_cog(Help(bot))