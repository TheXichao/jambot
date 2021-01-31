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

@client.event
async def on_ready():
  print('Bot is ready')


@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await updateData(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await updateData(users, message.author)
        await addExperience(users, message.author, 5)
        await levelUp(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)


async def updateData(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def addExperience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def levelUp(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')


@client.command()
async def spam(ctx,t,*,message):
  for _ in range(int(t)):
    await ctx.send(message)
    time.sleep(1)
    
@client.command(aliases=['8ball','is'])
async def _8ball(ctx,*,question):
  response = [
"As I see it, yes."
"Ask again later."
"Better not tell you now."
"Cannot predict now."
"Concentrate and ask again."
"Don’t count on it."
"It is certain."
"It is decidedly so."
"Most likely."
"My reply is no."
"My sources say no."
"Outlook not so good."
"Outlook good."
"Reply hazy, try again."
"Signs point to yes."
"Very doubtful."
"Without a doubt."
"Yes."
"Yes – definitely."
"You may rely on it."
  ]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

@client.command()
async def clear(ctx,amount=6):
  await ctx.channel.purge(limit=amount)
  
keep_alive()
client.run(os.getenv('TOKEN'))