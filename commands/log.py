import discord
from config import connection
from discord.ext import commands
import datetime

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        if ctx.author.bot or ctx.author.bot: return
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT log_channel_id FROM ServerConfig WHERE guild_id = {ctx.guild.id}")
            channel_id = cursor.fetchone()
            print(channel_id)
        channel = self.client.get_channel(id=channel_id.get('log_channel_id'))
        if channel != ctx.channel:
            embed = discord.Embed(title='Messages delete', color=0xff3434, timestamp=datetime.datetime.now())
            embed.add_field(name='Author:', value=ctx.author, inline=False)
            embed.add_field(name='Message:', value=f'"{ctx.content}"', inline=False)
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/669159790961754112/705912066648834068/Dont.png')

            for picture in ctx.attachments:
                if picture.filename.endswith(('.png', '.jpg', '.gif', '.jpeg', '.ico', '.svg')):
                    embed.set_image(url=picture.proxy_url)
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(Events(client))
