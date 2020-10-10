import discord
from discord.ext import commands

class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def cls(self, ctx, amount: int = 5):
        await ctx.message.delete()


def setup(client):
    client.add_cog(Clear(client))
