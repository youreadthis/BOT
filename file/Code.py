import discord # Подключаем библиотеку
import config
from discord.ext import commands

intents = discord.Intents.default() # Подключаем "Разрешения"
intents.message_content = True
progrgram_work = False
# Задаём префикс и интенты
bot = commands.Bot(command_prefix="$", intents=intents)
bad_words = []
file_of_word = open('Слова.txt','r', encoding='UTF-8')
data = file_of_word.read()
data =data.split()
for i in data:
    bad_words.append(i)
print(bad_words)
@bot.event
async def on_message(message):
    msg = message.content
    for i in bad_words:
        if i.lower() in msg.lower():
            await message.delete()
            await message.channel.send("Данное слово запрещенно")


bot.run(config.token)