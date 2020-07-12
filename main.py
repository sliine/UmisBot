import discord
import os
import config
from discord.ext import commands
from discord import utils, member

client = commands.Bot(command_prefix='.s')
client.remove_command('help')

@client.event
async def on_ready():
    activity = discord.Game(name="https://kosuhin.space")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f'{client.user.name} is started')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.Post_Id:
            channel = self.get_channel(payload.channel_id)  # получаем объект канала
            message = await channel.fetch_message(payload.message_id)  # получаем объект сообщения
            member = utils.get(message.guild.members,
                               id=payload.user_id)  # получаем объект пользователя который поставил реакцию

            try:
                emoji = str(payload.emoji)  # эмоджик который выбрал юзер
                role = utils.get(message.guild.roles, id=config.Roles[emoji])  # объект выбранной роли (если есть)

                if (len([i for i in member.roles if i.id not in config.Excroles]) <= config.Max_Roles_Per_User):
                    await member.add_roles(role)
                    print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
                else:
                    await message.remove_reaction(payload.emoji, member)
                    print('[ERROR] Too many roles for user {0.display_name}'.format(member))

            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))

@client.command()
async def reload(ctx, extensions):
    try:
        client.unload_extension(f'commands.{extensions}')
        client.load_extension(f'commands.{extensions}')
        print('Successfully')
        await ctx.send("Reload successfully")
    except Exception as ex:
        print(f'Load Error: {ex}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
        print(f'+ {filename}')

@client.event()
async def on_raw_reaction_add(self, payLoad):
    channel = self.get_channel(payLoad.channel_id)
    message = await channel.fetch_message(payLoad.message_id)
    message = utils.get(message.guild.members, id=payLoad.user_id)

    try:
        emoji = str(payLoad.emoji)
        role = utils.get(message.guild.roles, id=config.Roles[emoji])

        if(len([i for i in member.roles if i.id not in config.Excroles]) <= config.Max_Roles_Per_User):
            await member.add_roles(role)
            print('[SUCCESS] User {0.display_name} has been grandet with role {1.name}'.format(member, role))
        else:
            await message.remove_reaction(payLoad.emoji, member)
            except KeyError as e:
                print('[ERROR] KeyError, no role found for ' + emoji)
            except Exception as e:
                print(repr(e))



client.run(config.Token)
