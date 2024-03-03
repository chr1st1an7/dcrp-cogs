import disnake
from disnake.ext import commands
import re
import requests
import urllib.parse

class wolfram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Wolfram cog is online.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.content.startswith('.ask'):
            question = message.content[4:].strip()
            answer = ask_question(question)
            embed = disnake.Embed(description="**"+answer+"**", color=0x827abd)
            await message.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(wolfram(bot))

def ask_question(question):
  app_id = 'PWV8R7-TQ4LPW73YJ'
  encoded_question = urllib.parse.quote(question)
  api_url = f'https://api.wolframalpha.com/v1/result?appid={app_id}&i={encoded_question}'
  response = requests.get(api_url)
  if response.status_code == 200:
      answer = response.text
      return answer
  else:
      answer = "Please enter an appropirate question."
      return answer