import discord
from discord.ext import commands
import config

class Role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id != config.POST_ID:
            return
        if payload.user_id == self.client.user.id:
            return
        channel = self.client.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = discord.utils.get(message.guild.members, id=payload.user_id)
        emoji = None
        try:
            emoji = str(payload.emoji)
            role = discord.utils.get(message.guild.roles, id=config.ROLES[emoji])  # объект выбранной роли (если есть)
            roles = list(config.ROLES.values())
            sp = len([i for i in member.roles if i.id in roles])
            print(sp)
            if sp < config.MAX_ROLES_PER_USER:
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != config.POST_ID:
            return
        if payload.user_id == self.client.user.id:
            return
        channel = self.client.get_channel(payload.channel_id)  # получаем объект канала
        message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
        member = discord.utils.get(message.guild.members,
                                   id=payload.user_id)  # получаем объект пользователя который поставил реакцию
        emoji = None
        try:
            emoji = str(payload.emoji)  # эмоджик который выбрал юзер
            role = discord.utils.get(message.guild.roles, id=config.ROLES[emoji])  # объект выбранной роли (если есть)

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))


def setup(client):
    client.add_cog(Role(client))
