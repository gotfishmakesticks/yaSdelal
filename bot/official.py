import discord
import pickle
import os
from discord.ext import commands
from random import randint

with open("settings.ini", "rb") as file:
    settings = pickle.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)

charcreation = False
charcreator : discord.User
charmessage : discord.Message

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


#@bot.event
#async def on_message(message : discord.Message):
    #message.


@bot.command(name='editchar', help='Создаёт меню для редактирования персонажа')
async def editchar(ctx, name : str):
    await ctx.channel.send(f'Редактирование персонажа {name}. Нажмите на соответствующую реакцию для редактирования определённого параметра\n')


@bot.command(name='createchar', help='Создаёт пустого персонажа')
async def createchar(ctx, name : str):
    if not os.path.exists(rf'Characters\{name}'):
        os.makedirs(rf'Characters\{name}\pics')
        meta = {
            'name': name,
            'owner': ctx.message.author.id,
            'visible': '',
            'full': '',
            'picsdir': rf'Characters\{name}\pics',
            'picscount': 0,
            'visibleapplied': False,
            'fullapplied': False,
            'editing': False,
            'finished': False
                }
        with open(rf'Characters\{name}\meta.bin', 'wb') as f:
            pickle.dump(meta, f)
        print(meta)
        await ctx.channel.send(f"Успешно создан персонаж {name}. Редактируйте его через {settings['prefix']}editchar.")
    else:
        await ctx.channel.send("Это имя персонажа уже занято.")
    pass


@bot.command(name='dice', help='(кол-во кубов) (кол-во граней) - бросить XdY')
async def dice(ctx, amount : int, edges : int):
    author = ctx.author
    result = "[ "
    for i in range(amount):
        res = randint(1, edges)
        if res == 1:
            result += f"__{res}__, "
        elif res < edges:
            result += f"{res}, "
        else:
            result += f"**{res}**!, "
    result = result.rstrip(", ") + " ]"
    output = "{0.mention} бросил {1}d{2}\n> Результаты: {3}".format(author, amount, edges, result)
    print(output)
    await ctx.message.delete()
    await ctx.channel.send(output)


bot.run(settings['token'])
