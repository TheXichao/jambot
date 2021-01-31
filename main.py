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
  with open('users.json','r') as f:
    users = json.load(f)

    await  updateData(users, member)


    
  with open('users.json','w') as f:
    json.dump(users,f)


@client.event
async def on_message(message):
  with open('users.json','r') as f:
    users = json.load(f)

  await updateData(users, message.author)
  await addExperience(users,message.author, 5)
  await levelUp(users, message.author, message.channel)


  with open('users.json','w') as f:
    json.dump(users,f)

async def updateData(users,user):
  if not user.id in users:
    users[user.id] = {}
    users[user.id]['experience'] = 0
    users[user.id]['level'] = 1

async def addExperience(users, user, exp):
  users[user.id]['experience'] += exp

async def levelUp(users, user, channel):
  experience = users[user.id]['experience']
  lvlStart = users[user.id]['level']
  lvlEnd = int(experience ** (1/4))

  if lvlStart < lvlEnd:
    await client.send_message(channel,'Congrats {} has leveled up to level {}'.format(user.mention,lvlEnd))
    users[user.id]['level'] = lvlEnd

  

@client.event
async def on_member_remove(member):
  print(f'{member} died, we might miss them')





@client.command()
async def spam(ctx,t,*,message):
  for _ in range(int(t)):
    await ctx.send(message)
    time.sleep(1)
    


keep_alive()
client.run(os.getenv('TOKEN'))