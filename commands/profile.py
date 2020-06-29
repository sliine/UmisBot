import discord
from discord.ext import commands

class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        member = ctx.author if member is None else member
        roles = [role for role in member.roles if role.id != ctx.message.guild.id]
        print(roles)
        embed = discord.Embed(color=0x16ed07, title="User profile",
                              description="I am looking for nothing")
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="General Information:",
                        value="--------------------------------------------------------",
                        inline=False)
        embed.add_field(name="Date of registration:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=True)
        embed.add_field(name="Join to the server:",
                        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
                        inline=True)
        embed.add_field(name="Detailed information:",
                        value="--------------------------------------------------------",
                        inline=False)
        embed.add_field(name="Roles: ",
                        value=" ".join(['None.'] if len(roles) < 1 else [role.mention for role in roles]), inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Profile(client))
