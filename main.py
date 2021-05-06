import discord
import random
import time
import asyncio

from discord import client
from discord.ext import commands

token = 'ODM5OTgxNDEwODM1MzY1ODk5.YJRjpg.19irUrN5KMxifqkiIpC5X3zDV9M'
client = discord.Client()

possible_messages = ['hey ruby', 'hello ruby', 'whats up ruby', 'good morning ruby', 'howdy ruby', 'hi ruby', 'hola ruby']

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    for x in range(len(possible_messages)):
        if message.content.startswith(possible_messages[x]):
                await message.channel.send(f"Hey! {round(client.latency * 1000)}ms")

@client.event
async def on_ready():
    print("Bot is online")

@client.event
async def on_member_join(member):
    print(f'Welcome {member}!')



client.run(token)