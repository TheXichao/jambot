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
async def on_ready(message):
  print('Bot is ready')
  await message.channel.send(f'WHHAT {member} spawned!!')

@client.event
async def on_member_join(member,message):
  await message.channel.send(f'WHHAT {member} spawned!!')
  print(f'WHHAT {member} spawned!!')
  

@client.event
async def on_member_remove(member):
  print(f'{member} died')

@client.command()
async def boop(ctx):
  await ctx.send('Boo!')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {client.latency * 1000}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx,*,question):
  response = [
    'likely','maybe','unlikely','um sure', 'poopoo'
  ]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

@client.command()
async def clear(ctx,amount=6):
  await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *,reason='nope'):
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *,reason='no'):
  await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
  bannedUsers= await ctx.guild.bans()
  memberName, memberDiscriminator = member.split('#')

  for banEntry in bannedUsers:
    user = banEntry.user

    if(user.name,user.discriminator) == (memberName,memberDiscriminator):
      await ctx.guild.unban(user)
      await ctx.send('unbanned {user}'.format(user=memberName))
      return

keep_alive()
client.run(os.getenv('TOKEN'))