import discord
from discord.ext import commands

class ReactRole(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_raw_reaction_add(self,payload):
    if payload.message_id == 810291063859576883 and str(payload.emoji) == ('💯'):
      # member = discord.Object(payload.user_id)
      guild = self.client.get_guild(payload.guild_id)
      role = discord.utils.get(guild.roles, name="verified")
      # await member.add_roles(role)
      member_proxy = discord.Object(payload.user_id)
      member_proxy._state = guild._state  # or bot._connection
      member_proxy.guild = guild
      await discord.Member.add_roles(member_proxy, role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self,payload):
    if payload.message_id == 810291063859576883 and str(payload.emoji) == ('💯'):
      # member = discord.Object(payload.user_id)
      guild = self.client.get_guild(payload.guild_id)
      role = discord.utils.get(guild.roles, name="verified")
      # await member.add_roles(role)
      member_proxy = discord.Object(payload.user_id)
      member_proxy._state = guild._state  # or bot._connection
      member_proxy.guild = guild
      await discord.Member.remove_roles(member_proxy, role)



  @commands.Cog.listener()
  async def on_ready(self):
    print('react role has been enabled') 

def setup(client):
  client.add_cog(ReactRole(client))