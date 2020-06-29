import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.s')
client.remove_command('help')


@client.event
async def on_ready():
    activity = discord.Game(name="https://kosuhin.space")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print(f'{client.user.name} is started')


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

client.run('')
