import discord
from discord.ext import commands
import datetime

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        if ctx.author.bot or ctx.author.bot: return
        channel = self.client.get_channel(id=715206327840014366)
        if channel != ctx.channel:
            embed = discord.Embed(title='Messages delete', color=0xff3434, timestamp=datetime.datetime.now())
            embed.add_field(name='Author:', value=ctx.author, inline=False)
            embed.add_field(name='Messahe:', value=ctx.content, inline=False)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/669159790961754112/705912066648834068/Dont.png')
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(Events(client))
