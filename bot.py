# This Python file uses the following encoding: utf-8
# bot.py

import os, sys

import discord
from discord.ext import commands
from dotenv import load_dotenv
import re
import asyncio

import csv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='$', activity=discord.Activity(type=discord.ActivityType.listening, name="God's words"), status=discord.Status.online, help_command = commands.DefaultHelpCommand(no_category = 'Commands'))

@bot.command(pass_context = True, aliases=['godC', 'holyC', 'heavenC', 'verseC', 'bible-verseC', 'biblec', 'godc', 'holyc', 'heavenc', 'versec', 'bible-versec'], help='| Usage: $bibleC <book_name(WITH DASHES)> <chapter_number> <verse_number> Eg: $bible 1-John 3 16, for 1 John 3:16 verse. Returns a bible verse(Union - simplified chinese). For a list of books, use $bibleC books.')
async def bibleC(ctx, arg1=None, arg2=None, arg3=None, arg4=None):

    book = arg1
    ch = arg2
    v = arg3
    end = arg4
    text = ""
    booklist = []
    clbooklist = ['书 名', '創 世 記', '出 埃 及 記', '利 未 記', '民 數 記', '申 命 記', '約 書 亞 記', '士 師 記', '路 得 記', '撒 母 耳 記 上', '撒 母 耳 記 下', '列 王 紀 上', '列 王 紀 下', '歷 代 志 上', '歷 代 志 下', '以 斯 拉 記', '尼 希 米 記', '以 斯 帖 記', '約 伯 記', '詩 篇', '箴 言', '傳 道 書', '雅 歌', '以 賽 亞 書', '耶 利 米 書', '耶 利 米 哀 歌', '以 西 結 書', '但 以 理 書', '何 西 阿 書', '約 珥 書', '阿 摩 司 書', '俄 巴 底 亞 書', '約 拿 書', '彌 迦 書', '那 鴻 書', '哈 巴 谷 書', '西 番 雅 書', '哈 該 書', '撒 迦 利 亞', '瑪 拉 基 書', '馬 太 福 音', '馬 可 福 音', '路 加 福 音', '約 翰 福 音', '使 徒 行 傳', '羅 馬 書', '歌 林 多 前 書', '歌 林 多 後 書', '加 拉 太 書', '以 弗 所 書', '腓 立 比 書', '歌 羅 西 書', '帖 撒 羅 尼 迦 前 書', '帖 撒 羅 尼 迦 後 書', '提 摩 太 前 書', '提 摩 太 後 書', '提 多 書', '腓 利 門 書', '希 伯 來 書', '雅 各 書', '彼 得 前 書', '彼 得 後 書', '約 翰 一 書', '約 翰 二 書', '約 翰 三 書', '猶 大 書', '启 示 录']
    engbooklist = ['Book Name', 'genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', '1-samuel', '2-samuel', '1-kings', '2-kings', '1-chronicles', '2-chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'song of solomon', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi', 'matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1-corinthians', '2-corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1-thessalonians', '2-thessalonians', '1-timothy', '2-timothy', 'titus', 'philemon', 'hebrews', 'james', '1-peter', '2-peter', '1-john', '2-john', '3-john', 'jude', 'revelation']
    prevbook = "书 名"
    books = ""

    with open("union.csv", mode='r', encoding="UTF-8") as f:
        mycsv = csv.reader(f)
            
        if arg1 == "books":
            for row in mycsv:
                if row[1] != prevbook:

                    booklist.append(row[1])
                    prevbook = row[1]

            for i, j in enumerate(booklist):
                books += f"{i+1}) {j}; "

            await ctx.send(books)

        elif arg2 and arg3 and arg4:

            try:

                int(arg4)
                int(arg3)
                int(arg2)
        
                for row in mycsv:

                    for i in range(int(arg3), int(arg4) + 1):

                        try:

                            if (int(clbooklist.index(row[1])) == int(engbooklist.index(book.lower()))) and row[3] == ch and row[4] == str(i):
                                text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                                await ctx.send(text)

                        except:

                            if row[2] == book and row[3] == ch and row[4] == str(i):
                                text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                                await ctx.send(text)

                if text == "":
                    await ctx.send("Invalid Input!")

            except:
                await ctx.send("Invalid Input!")

        elif arg2 and arg3:

            try:

                int(arg3)
                int(arg2)

                for row in mycsv:

                    try:

                        if (int(clbooklist.index(row[1])) == int(engbooklist.index(book.lower()))) and row[3] == ch and row[4] == v:
                            text = f"{row[1]} {ch}:{v} {row[5]}"

                    except:

                        if row[2] == book and row[3] == ch and row[4] == v:
                            text = f"{row[1]} {ch}:{v} {row[5]}"

                if text == "":
                    await ctx.send("Invalid Input!")

                else:
                    await ctx.send(text)

            except:
                await ctx.send("Invalid Input!")

        elif arg2:

            try:

                int(arg2)

                for row in mycsv:

                    try:

                        if (int(clbooklist.index(row[1])) == int(engbooklist.index(book.lower()))) and row[3] == ch:
                            text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                            await ctx.send(text)

                    except:

                        if row[2] == book and row[3] == ch:
                            text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                            await ctx.send(text)
                
                if text == "":
                    await ctx.send("Invalid Input!")

            except:
                await ctx.send("Invalid Input!")

        else:
            await ctx.send("Invalid Input!")

@bot.command(pass_context = True, aliases=['biblesearch', 'bibles', 'gods', 'holys', 'heavens', 'verses', 'bible-verses', 'godS', 'holyS', 'heavenS', 'verseS', 'bible-verseS', 'godsearch', 'holysearch', 'heavensearch', 'versesearch', 'bible-versesearch'], help="| Usage: $bibleS <String_to_search_here>")
async def bibleS(ctx, *, arg1):

    try:

        int(arg1)

        await ctx.send("Invalid Input! Only strings allowed, no numbers!")

    except:

        await ctx.send(f"Confirm '{arg1}' as query?")

        try:

            reply_message = await bot.wait_for('message', timeout=15.0)

        except asyncio.TimeoutError:
            await ctx.send('Time out!')

        else:

            if reply_message.content.lower() == ('yes' or 'y' or 'yeah' or 'yessi'):

                with open("kjv.csv", mode='r') as f:
                    mycsv = csv.reader(f)

                    for row in mycsv:
                        if re.search(arg1, row[5]):
                            text = f"{row[1]} {row[3]}:{row[4]} {row[5]}"
                            await ctx.send(text)

                    if text == "":
                        await ctx.send("String not found.")

            else:

                await ctx.send("Please try again.")

@bot.command(pass_context = True, aliases=['biblecsearch', 'biblecS', 'godcs', 'holycs', 'heavencs', 'versecs', 'bible-versecs', 'godcS', 'holycS', 'heavencS', 'versecS', 'bible-versecS', 'godcsearch', 'holycsearch', 'heavencsearch', 'versecsearch', 'bible-versecsearch', 'bibleCs', 'biblecs', 'godCs', 'holyCs', 'heavenCs', 'verseCs', 'bible-verseCs', 'godCS', 'holyCS', 'heavenCS', 'verseCS', 'bible-verseCS', 'godCsearch', 'holyCsearch', 'heavenCsearch', 'verseCsearch', 'bible-verseCsearch'], help="| Usage: $bibleCS <String_to_search_here>")
async def bibleCS(ctx, *, arg1):

    try:

        int(arg1)

        await ctx.send("Invalid Input! Only strings allowed, no numbers!")

    except:

        with open("kjv.csv", mode='r', encoding="UTF-8") as f:
            mycsv = csv.reader(f)

            for row in mycsv:
                if re.search(arg1, row[5]):
                    text = f"{row[1]} {row[3]}:{row[4]} {row[5]}"
                    await ctx.send(text)

            if text == "":
                await ctx.send("String not found.")

@bot.command(pass_context = True, aliases=['god', 'holy', 'heaven', 'verse', 'bible-verse'], help='| Usage: $bible <book_name(WITH DASHES)> <chapter_number> <verse_number> Eg: $bible 1-John 3 16, for 1 John 3:16 verse. Returns a bible verse(KJV). For a list of books, use $bible books')
async def bible(ctx, arg1=None, arg2=None, arg3=None, arg4=None):

    book = arg1
    ch = arg2
    v = arg3
    end = arg4
    text = ""
    booklist = []
    prevbook = "Book Name"
    books = ""

    with open("kjv.csv", 'r') as f:
        mycsv = csv.reader(f)

        if arg1 == "books":

            for row in mycsv:
                if row[1] != prevbook:

                    booklist.append(row[1])
                    prevbook = row[1]

            for i, j in enumerate(booklist):
                books += f"{i+1}) {j}; "

            await ctx.send(books)


        elif arg2 and arg3 and arg4:

            try:

                int(arg4)
                int(arg3)
                int(arg2)

                for row in mycsv:

                    for i in range(int(arg3), int(arg4) + 1):

                        if row[1].lower() == book.lower() and row[3] == ch and row[4] == str(i):
                            text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                            await ctx.send(text)

                        elif row[2] == book and row[3] == ch and row[4] == str(i):
                            text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                            await ctx.send(text)

                if text == "":
                    await ctx.send("Invalid Input!")

            except:
                await ctx.send("Invalid Input!")

        elif arg2 and arg3:

            try:

                int(arg3)
                int(arg2)

                for row in mycsv:

                    if row[1].lower() == book.lower() and row[3] == ch and row[4] == v:
                        text = f"{row[1]} {ch}:{v} {row[5]}"

                    elif row[2] == book and row[3] == ch and row[4] == v:
                        text = f"{row[1]} {ch}:{v} {row[5]}"

                if text == "":
                    await ctx.send("Invalid Input!")

                else:
                    await ctx.send(text)

            except:
                await ctx.send("Invalid Input!")

        elif arg2:
            
            try:

                int(arg2)

                for row in mycsv:

                    if row[1].lower() == book.lower() and row[3] == ch:
                        text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                        await ctx.send(text)

                    elif row[2] == book and row[3] == ch:
                        text = f"{row[1]} {ch}:{row[4]} {row[5]}"
                        await ctx.send(text)
                
                if text == "":
                    await ctx.send("Invalid Input!")

            except:
                await ctx.send("Invalid Input!")

        else:
            await ctx.send("Invalid Input!")

                



bot.run(TOKEN)