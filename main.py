import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands
import time

def get_prefix(client,message):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix= get_prefix)


@client.command()
@commands.has_permissions(manage_guild = True)
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')


@client.command()
@commands.has_permissions(manage_guild = True)
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_guild_join(guild):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)
  prefixes[str(guild.id)] = '.'

  with open('prefixes.json','w') as f:
    json.dump(prefixes, f, indent=4)

@client.event
async def on_guid_remove(guild):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)
  prefixes.pop(str(guild.id))

  with open('prefixes.json','w') as f:
    json.dump(prefixes, f)

@client.command()
@commands.has_permissions(administrator = True)
async def set_prefix(ctx,prefix):
  with open('prefixes.json','r') as f:
    prefixes = json.load(f)

  prefixes[str(ctx.guild.id)] = prefix

  with open('prefixes.json','w') as f:
    json.dump(prefixes, f)
  await ctx.send(f'Prefix is now {prefix}')



keep_alive()
client.run(os.getenv('TOKEN'))
