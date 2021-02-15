import discord
from discord.ext import commands
from random import random

class general(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.command()
  async def ping(self,ctx):
    await ctx.send('Pong!')

  @commands.Cog.listener()
  async def on_ready(self):
    print('general_commands has been loaded')

  
  @commands.command(aliases=['8ball','is'])
  async def _8ball(self, ctx,*,question):
    response = [
  "As I see it, yes.",
  "Ask again later.",
  "Better not tell you now.",
  "Cannot predict now.",
  "Concentrate and ask again.",
  "Don’t count on it.",
  "It is certain.",
  "It is decidedly so.",
  "Most likely.",
  "My reply is no.",
  "My sources say no.",
  "Outlook not so good.",
  "Outlook good.",
  "Reply hazy, try again.",
  "Signs point to yes.",
  "Very doubtful.",
  "Without a doubt."
  "Yes.",
  "Yes – definitely.",
  "You may rely on it."
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')
      
def setup(client):
  client.add_cog(general(client))