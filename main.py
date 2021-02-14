import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import time

client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx,extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
    


keep_alive()
client.run(os.getenv('TOKEN'))