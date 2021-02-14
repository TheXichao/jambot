import discord
from discord.ext import commands

class Example(commands.Cog):

  def __init__(self,client):
    self.clent = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('bot is online.')

  @commands.command()
  async def ping(self,ctx):
    await ctx.send('Pong!')

def setup(client):
  client.add_cog(Example(client))