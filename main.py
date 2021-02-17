import json
import os
import random
import time

import discord
import requests
from discord.ext import commands
from replit import db

from keep_alive import keep_alive


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix,
                      intents=discord.Intents.all(), owner_id=536244741394923532)
# client.remove_command('help')


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename[:-3]} has been loaded')


@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guid_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)


@client.command()
@commands.has_permissions(administrator=True)
async def set_prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f)
    await ctx.send(f'Prefix is now {prefix}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You are missing a required argument.")
    elif isinstance(error, commands.MissingPermissions):
        if len(error.missing_perms) == 1:
            perms = ''.join(error.missing_perms)
        else:
            perms = ', '.join(error.missing_perms)
        await ctx.reply(f"You need the following perms: `{perms}`.")
    elif isinstance(error, commands.BotMissingPermissions):
        if len(error.missing_perms) == 1:
            perms = ''.join(error.missing_perms)
        else:
            perms = ', '.join(error.missing_perms)
        await ctx.reply(f"I need the following perms: `{perms}`.")

    debug = client.get_user(client.owner_id)
    await debug.send(f"Error in **{ctx.guild.name}**:\n```{str(error)}```")
    raise error


@client.event
async def on_ready():
  await client.wait_until_ready()
  print(f'the bot has logged in as {client.user}')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you'))


# @client.group(invoke_without_command=
# True)
# async def help(ctx):

#   em = discord.Embed(title = 'help')

# @client.command()
# await def help(ctx)

keep_alive()
client.run(os.getenv('TOKEN'))
