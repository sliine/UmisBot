import discord
from discord.ext import commands

class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.command()
        @client.has_permissions(administrator = True)
        async def mute(self, ctx, member: discord.Member):
            await ctx.channel.purge(limit = 1)
            mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')
            await member.add_roles(mute_role)
            await ctx.send(f'User {member.mention}, has bean muted! ')


def setup(client):
    client.add_cog(Mute(client))

