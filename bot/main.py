import discord
import pickle
from discord.ext import commands
from random import randint, random

with open("rpconfig.ini", "rb") as file:
    rpmode = pickle.load(file)
with open("settings.ini", "rb") as file:
    settings = pickle.load(file)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


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


@bot.command(name = '', help = '(имя персонажа) "(текст)" - вывести сообщение от лица персонажа (текст должен быть в кавычках)')
async def play(ctx, char : str, msg : str):
    message = msg
    output = f'`{char}`: {message}'
    await ctx.message.delete()
    await ctx.channel.send(output)


@bot.command(name = 'chrlistcreate', help = '(имя персонажа) (ссылка) - создать лист персонажа')
async def chrlistcreate(ctx, char, url):
    fname = f"{char}.chr"
    try:
        with open(fname, 'wb') as file:
            pickle.dump(url, file)
            print(fname + " created!")
        ret = f"Создан лист персонажа {char}."
        await ctx.channel.send(ret)
    except:
        print(f"Не удалось записать в {fname}")
        await ctx.channel.send(f"Не удалось создать лист персонажа {char}!")


@bot.command(name = 'chrlist', help = '(имя персонажа) - вывести лист персонажа, если имеется')
async def chrlist(ctx, char):
    fname = f'{char}.chr'
    try:
        with open(fname, 'rb') as file:
            url : str = pickle.load(file)
        await ctx.channel.send(url)
    except:
        print(f'Не удалось открыть {fname}')
        await ctx.channel.send(f"Не удалось найти лист персонажа {char}!")


@bot.command(name = 'chrlore', help = '(имя персонажа) - вывести текст об этом персонаже, если имеется')
async def chrlore(ctx, char):
    sent = 0
    fname = f"{char}0.txt"
    try:
        for i in range(10):
            fname = f"{char}{i}.txt"
            file = discord.File(fname)
            await ctx.channel.send(file=file)
            sent += 1
    except:
        print(f"Не найден {fname}!")
        if sent == 0:
            await ctx.channel.send("Не удалось найти текст персонажа")
        else:
            await ctx.channel.send(f"Найден(о) {sent} файл(ов)")


@bot.command(name = 'chrlorecreate', help = '(имя персонажа) (файл в формате .txt) - создать текст об этом персонаже')
async def chrlorecreate(ctx, char):
    message = ctx.message
    atts : list = message.attachments
    if atts:
       for i in range(len(atts)):
           await atts[i].save(f"{char}{i}.txt")
       await ctx.channel.send(f"Сохранен(о) {len(atts)} файл(ов).")
    else:
        await ctx.channel.send("Не удалось найти файлы")


@bot.command(name = settings['prefix'], help = 'Различные функции, объединённые в одну')
async def doldol(ctx, arg1 : str):
    dicebool = True
    dicecheck = arg1.split("d", 2)
    print(dicecheck)
    try:
        diceamount = int(dicecheck[0])
        diceedges = int(dicecheck[1])
        await dice(ctx, diceamount, diceedges)
    except:
        print("Это не XdY")
        dicebool = False


@bot.command(name = 'rp', help = 'Переключает RP режим бота')
async def botrp(ctx):
    global rpmode
    if rpmode:
        rpmode = False
        await ctx.channel.send("RP режим бота выключен, спасибо за игру!")
    else:
        rpmode = True
        await ctx.channel.send("RP режим бота включён. Приятной игры!")
    with open("rpconfig.ini", "wb") as file:
        pickle.dump(rpmode, file)


@bot.command(name = "chrlink", help = "(имя персонажа) - Привязать персонажа к игроку")
async def chrlink(ctx, char):
    author = ctx.message.author.id
    fname = "rp.cfg"
    with open(fname, "rb") as file:
        dict = pickle.load(file)
    dict.update({f'{author}' : f'{char}'})
    with open(fname, "wb") as file:
        pickle.dump(dict, file)
    print(dict)
    await ctx.channel.send(f"Вы прикреплены к персонажу {char}.")


@bot.command(name = "prefix", help = "(новый префикс) - меняет префикс команд. Требует перезапуска.")
async def prefix(ctx, prefix):
    settings['prefix'] = prefix
    with open("settings.ini", "wb") as file:
        pickle.dump(settings, file)
    await ctx.channel.send(f"Префикс бота изменён на `{prefix}`. Для применения изменений перезапустите бота.")


@bot.command(name = 'qp', help = '"(текст)" - быстрый ввод play без персонажа, если он прикреплен к пользователю')
async def qp(ctx, text):
    author = ctx.message.author.id
    with open("rp.cfg", "rb") as file:
        dict = pickle.load(file)
    char = dict[f'{author}']
    try:
        await play(ctx, char, text)
    except:
        await ctx.channel.send(f"К вам не прикреплён персонаж! Сделайте это через {settings['prefix']}chrlink.")


bot.run(settings['token'])
