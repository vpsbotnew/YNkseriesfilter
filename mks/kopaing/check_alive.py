import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("š”šš½š½š šØšŗš š šššš¾ :) š§šš /start \n\nš§šš /help š„šš š§š¾šš ;)\n\n\nš§šš /ping š³š š¢šš¾š¼š š”šš šÆššš š")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("š§šš /movie š„šš š¬šššš¾ š²š¾šŗšš¼š š±ššš¾š š\n\nš§šš /series š„šš š²š¾ššš¾š š²š¾šŗšš¼š š±ššš¾š š\n\n\nš§šš /tutorial š„šš šÆšššš¾š š³ššššššŗš šµšš½š¾šš š¤")


@Client.on_message(filters.command("movie", CMD))
async def movie(_, message):
    await message.reply_text("ā ļøāļø š š¼šš¶š² š„š²š¾šš²šš šš¼šæšŗš®š āļø")

@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("ā ļøāļø š¦š²šæš¶š²š š„š²š¾šš²šš šš¼šæšŗš®š āļø")

@Client.on_message(filters.command("tutorial", CMD))
async def tutorial(_, message):
    await message.reply_text("š¢šš¾š¼šššš š")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"šÆššš!\n{time_taken_s:.3f} ms")
