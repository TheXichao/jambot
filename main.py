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

@client.command
async def ping(ctx):
  await ctx.send(f'Pong! {client.latency * 1000}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
  response = [
    'likely','maybe','unlikely','um sure', 'poopoo'
  ]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')





keep_alive()
client.run(os.getenv('TOKEN'))