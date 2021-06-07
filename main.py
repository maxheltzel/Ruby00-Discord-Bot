import asyncio
import random
import _json
from discord import client
import requests
from discord.ext import commands
import discord
from discord.ext.commands import bot
import re
import json
from datetime import datetime, time
from keep_alive import keep_alive

token = 'insert token'
bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Bot is online")

@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.channel.send('Pong!')

@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is Certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.',
                 'As I see it, yes.', 'Most likely.', 'Yes', 'Signs point to yes.','My reply is no.', 'My sources say no.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def findCoincidences(w):
    return re.compile(r'\b({0})\b'.format(w)).search

@bot.listen()  # react to messages
async def on_message(message):
    if message.guild is not None:
        content = message.content
    reaction = "👋"
    if 'hi' in content.lower():
        try:
            await asyncio.sleep(1)
            await message.add_reaction(f"<{reaction}>")
            print(f'added reaction {reaction} {content}')
        except Exception as e:
            print(f'error adding reaction {reaction} {content}')
    if 'hello' in content.lower():
        try:
            await asyncio.sleep(1)
            await message.add_reaction(f"<{reaction}>")
            print(f'added reaction {reaction} {content}')
        except Exception as e:
            print(f'error adding reaction {reaction} {content}')
    if 'howdy' in content.lower():
        try:
            await asyncio.sleep(1)
            await message.add_reaction(f"<{reaction}>")
            print(f'added reaction {reaction} {content}')
        except Exception as e:
            print(f'error adding reaction {reaction} {content}')
    if 'hey' in content.lower():
        try:
            await asyncio.sleep(1)
            await message.add_reaction(f"<{reaction}>")
            print(f'added reaction {reaction} {content}')
        except Exception as e:
            print(f'error adding reaction {reaction} {content}')
    await bot.process_commands(message)

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

@bot.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def dm(ctx, member: discord.Member = None, message=None, b=None):
    if member == None:
        await ctx.send('Mention a member')
        return
    if b == None:
        c = 1
    elif int(b) > 10:
        c = 10
    else:
        c = int(b)
    for a in range(c):
        await member.send(message)

    await clear(ctx)

delay = 1800  # seconds
discordWebhook = 'add your webhook'

def getPrice(currency):
    priceUrl = 'https://api.coinbase.com/v2/prices/{}-USD/spot'.format(currency)
    r = requests.get(priceUrl)
    r = json.loads(r.text)
    return r['data']['amount']

def getVolume(currency):
    priceUrl = 'https://api.coinbase.com/v2/prices/{}-USD/spot'.format(currency)
    r = requests.get(priceUrl)
    r = json.loads(r.text)
    print(r)

    priceUrl = 'https://api.coinbase.com/v2/exchange-rates?currency=BTC'.format(currency)

@bot.command(pass_context=True)
async def coin(ctx, *, coin_name):
    while True:
        coin_price = getPrice(coin_name.upper())
        timestamp = datetime.utcnow().replace(microsecond=0).isoformat()
        embeds = [{
            'type': 'rich',
            "color": 0xf1c40f,
            "timestamp": timestamp,
            "fields": [{"name": f"{coin_name.upper()}", "value": "$" + str(coin_price), "inline": True}]
        }]
        payload = {"embeds": embeds}
        r = requests.post(discordWebhook, json=payload)
        time.sleep(delay)
        await ctx.send(r)

getVolume('BTC')
bot.run(token)
