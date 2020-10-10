import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        emb = discord.Embed(title='Help commands for bots',
                            color=0x16ed07)
        emb.add_field(name='.sping', value="Check your ping",
                      inline=False)
        emb.add_field(name='.sprofile', value="Check information or your profile",
                      inline=False)
        emb.add_field(name='.sslap', value="Just Fun:)",
                      inline=False)
        emb.add_field(name='.ssetup', value="SetUp settings bots",
                      inline=False)
        await ctx.send(embed=emb)


def setup(client):
    client.add_cog(Help(client))
