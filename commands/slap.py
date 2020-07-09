import discord
from discord.ext import commands

class Slap(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def slap(self, ctx, member: discord.Member = None):
        member = ctx.author if member is None else member
        embed = discord.Embed(
            color=0x16ed07,
            description=f'User **{ctx.author.name}** prescribed bread in the face **{member.name}**'
        )
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Slap(client))