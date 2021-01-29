import json
import asyncio
import discord
import logging
from discord.ext import commands
import math

#Retrieve token from config.json
with open('config.json') as jsonData:
    Token = json.load(jsonData)
    Token = Token.get('Token')

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix ='.')


@bot.event
async def on_ready():
    print('Bot Online')


@bot.command()
async def ping(ctx):
    '''Displays latency'''
    await ctx.send("{0}ms".format(math.floor(bot.latency*1000)))


bot.run(Token)
