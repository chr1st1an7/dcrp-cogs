import disnake
from disnake.ext import commands
import urllib.parse
import aiohttp

class wolfram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Wolfram cog is online.')

    @commands.command()
    async def ask(self, ctx, *, arg):
            answer = await ask_question(arg)
            message = ctx.message
            embed = disnake.Embed(description="**"+answer+"**", color=0x827abd)
            await message.reply(embed=embed, mention_author=False)

def setup(bot):
    bot.add_cog(wolfram(bot))

async def ask_question(question):
    app_id = 'PWV8R7-TQ4LPW73YJ'
    encoded_question = urllib.parse.quote(question)
    api_url = f'https://api.wolframalpha.com/v1/result?appid={app_id}&i={encoded_question}'

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                answer = await response.text()
                return answer
            else:
                answer = "Please enter an appropriate question."
                return answer
