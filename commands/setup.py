import discord
import json
from config import connection
from discord.ext import commands

class Setup(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("languages.json", "r", encoding="utf-8") as file:
            self.languages = json.loads(file.read())

    @commands.command()
    async def setup(self, ctx, lang: str = 'ru', prefix: str = '~'):
        if lang not in ['ru', 'en']:
            await ctx.send('Язык не поддерживается. Доступные языки: ``ru, en``')
            return
        if len(prefix) > 5:
            await ctx.send('Префикс слишком длинный')
            return
        languages = self.languages
        check = await ctx.send(languages[lang]['Check'])

        log_channel = None
        error_channel = None

        try:
            if discord.utils.get(ctx.guild.categories, name='Umis'):
                print('Umis category - Yes')
                await check.edit(content=languages[lang]['Umis_Check_Yes'])
                category = discord.utils.get(ctx.guild.categories, name='Shine')
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

            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM ServerConfig WHERE guild_id = {ctx.guild.id}")
                if cursor.fetchone() is None:
                    cursor.execute(
                        f"""INSERT INTO ServerConfig (guild_id, lang, guild_prefix, log_channel_id, error_channel_id)
                                        VALUES ({ctx.guild.id}, '{lang}', '{prefix}', {log_channel.id}, {error_channel.id});""")
                else:
                    cursor.execute(
                        f"""UPDATE ServerConfig SET 
                            guild_id = {ctx.guild.id}, 
                            lang = '{lang}',
                            guild_prefix = '{prefix}', 
                            log_channel_id = {log_channel.id}, 
                            error_channel_id = {error_channel.id} 
                            WHERE guild_id = {ctx.guild.id}""")

                connection.commit()
                print(languages[lang]['Complete'])
            await check.edit(content=languages[lang]['Complete'])
        except Exception as ex:
            print(f"{languages[lang]['Error']} ``{ex}``**")
            await check.edit(content=f"{languages[lang]['Error']} ``{ex}``**")

def setup(client):
    client.add_cog(Setup(client))
