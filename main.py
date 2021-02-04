import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands

cogs = [levelsys]

client = commands.Bot(command_prefix='.',intents=discord.intents.all())

for _ in range(len(cogs)):
  print('hi')


keep_alive()
client.run(os.getenv('TOKEN'))