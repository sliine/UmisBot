import discord
from discord.ext import commands
import pymysql
from contextlib import closing
from pymysql.cursors import DictCursor

config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
}

connection = pymysql.connect(host=config.get('host'),
                             user=config.get('user'),
                             password=config.get('password'),
                             db=config.get('database'),
                             charset='utf8mb4',
                             cursorclass=DictCursor)

connection.close()

class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.languages = {
            'ru': {
                "Check": "**Проверка ...**",
                "Umis_Check_Yes": "**Категория** ``Umis`` **существует.**",
                "Umis_Check_No": "**Категории** ``Umis`` **не существует.**",
                "Umis_Check": "**Категория** ``Umis`` **получена.**",
                "Umis_Check_Created": "**Категория** ``Umis`` **создана.**",

                "Umis_Check_Log_Yes": "**Канал** ``📜logs`` **существует.**",
                "Umis_Check_Log_Created": "**Канал** ``📜logs`` **создан.**",
                "Umis_Check_Log_No": "**Канала** ``📜logs`` **не существует.**",
                "Umis_Check_Error_Yes": "**Канал** ``📜errors`` **существует.**",
                "Umis_Check_Error_Created": "**Канал** ``📜errors`` **создан.**",
                "Umis_Check_Error_No": "**Канала** ``📜errors`` **не существует.**",

                "Complete": "**Успешно.**",
                "Error": "**Ошибка.**",
            },
            'en': {
                "Check": "**Check ...**",
                "Umis_Check_Yes": "**Category** ``Shine`` **exists.**",
                "Umis_Check_No": "**Categories** ``Shine`` **does not exists.**",
                "Umis_Check": "**Category** ``Shine`` **received.**",
                "Umis_Check_Created": "**Category** ``Shine`` **created.**",

                "Umis_Check_Log_Yes": "**Channel** ``📜logs`` **exists.**",
                "Umis_Check_Log_Created": "**Channel** ``📜logs`` **created.**",
                "Umis_Check_Log_No": "**Channel** ``📜logs`` **does not exists.**",
                "Umis_Check_Error_Yes": "**Channel** ``📜errors`` **exists.**",
                "Umis_Check_Error_Created": "**Channel** ``📜errors`` **created.**",
                "Umis_Check_Error_No": "**Channel** ``📜errors`` **does not exists.**",

                "Complete": "**Successfully.**",
                "Error": "**Error.**",
            },
        }

    # lang = 'en'

    @commands.command()
    async def setup(self, ctx, lang: str = 'ru', prefix: str = '~'):
        if lang not in ['ru', 'en']:
            await ctx.send('Язык не поддерживается. Доступные языки: ``ru, en``')
            return
        languages = self.languages
        check = await ctx.send(languages[lang]['Check'])

        log_channel = None
        error_channel = None

        try:
            if discord.utils.get(ctx.guild.categories, name='Umis'):
                print('Umis category - Yes')
                await check.edit(content=languages[lang]['Umis_Check_Yes'])
                category = discord.utils.get(ctx.guild.categories, name='Umis')
                await check.edit(content=languages[lang]['Umis_Check'])
                if discord.utils.get(ctx.guild.channels, name='📜logs'):
                    print('📜logs - Yes')
                    log_channel = discord.utils.get(ctx.guild.channels, name='📜logs')
                    await check.edit(content=languages[lang]['Umis_Check_Log_Yes'])
                else:
                    print('📜logs - No')
                    await check.edit(content=languages[lang]['Umis_Check_Log_No'])
                    log_channel = await category.create_text_channel('📜logs')
                    await check.edit(content=languages[lang]['Umis_Check_Log_Created'])

                if discord.utils.get(ctx.guild.channels, name='📜errors'):
                    print('📜error - Yes')
                    error_channel = discord.utils.get(ctx.guild.channels, name='📜errors')
                    await check.edit(content=languages[lang]['Umis_Check_Error_Yes'])
                else:
                    print('📜error - No')
                    await check.edit(content=languages[lang]['Umis_Check_Error_No'])
                    error_channel = await category.create_text_channel('📜errors')
                    await check.edit(content=languages[lang]['Umis_Check_Error_Created'])
            else:
                print('Umis category - No')
                await check.edit(content=languages[lang]['Umis_Check_No'])
                category = await ctx.guild.create_category('Umis')
                print('Категория создана.')
                await check.edit(content=languages[lang]['Umis_Check_Created'])
                log_channel = await category.create_text_channel('📜logs')
                await check.edit(content=languages[lang]['Umis_Check_Log_Created'])
                error_channel = await category.create_text_channel('📜errors')
                await check.edit(content=languages[lang]['Umis_Check_Error_Created'])

            post1 = {
                "_id": ctx.guild.id,
                'lang': lang,
                'prefix': prefix,
                'log_channel_id': log_channel.id if log_channel else None,
                'error_channel_id': error_channel.id if error_channel else None
            }

            # pymysql.Server_Config.update({"_id": ctx.guild.id}, post1, upsert=True)
            with connection.cursor() as cursor:
                cursor.execute(f"""  INSERT INTO ServerConfig (guild_id, guild_prefix, log_channel_id, error_channel_id)
                                    VALUES (111, '222', 234234, 324234);""")
                print(languages[lang]['Complete'])
                connection.commit()
            await check.edit(content=languages[lang]['Complete'])
        except Exception as ex:
            print(f"{languages[lang]['Error']} ``{ex}``**")
            await check.edit(content=f"{languages[lang]['Error']} ``{ex}``**")

def setup(client):
    client.add_cog(Setup(client))
