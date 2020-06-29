import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        emb = discord.Embed(
            title='Your Ping', color=0x16ed07,
            description=f'{self.client.latency * 1000:.0f} ms'
        )
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Ping(client))