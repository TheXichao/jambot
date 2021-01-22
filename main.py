import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready')

@client.event
async def on_member_join(member):
  print(f'WHHAT {member} spawned!!')

@client.event
async def on_member_remove(member):
  print(f'{member} died')

@client.command()
async def boop(ctx):
  await ctx.send('Boo!')







keep_alive()
client.run(os.getenv('TOKEN'))