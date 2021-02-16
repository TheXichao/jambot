import discord
from discord.ext import commands
import time

class moderation(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx,member : discord.Member, *,reason=None):
    await member.kick(reason=reason)
    if reason == None:
      await ctx.send(f'{member} has been kicked.')
    else:
      await ctx.send(f'{member} has been kicked for {reason}.')

  
  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def ban(self,ctx,member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    if reason == None:
      await ctx.send(f'{member.mention} has been banned.')
    else:
      await ctx.send(f'{member.mention} has been banned for {reason}.')

  @commands.command()
  @commands.has_permissions(ban_members = True)
  async def unban(self, ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name , member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry
      if (user.name,user.discriminator) == (member_name,member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'{user.mention} has been unbanned, {user.name} is now free to rejoin')
        return

  @commands.command()
  @commands.has_permissions(manage_channels = True)
  async def spam(self,ctx,repetitions = 3,*,message):
    for _ in range(int(repetitions)):
      await ctx.send(message)
      time.sleep(1)

  @commands.command()
  @commands.has_permissions(manage_channels = True)
  async def clear(self,ctx,amount = 5):
    await ctx.channel.purge(limit = amount)
    print(f'{ctx.author} cleared {amount} messages')

  @commands.command()
  @commands.has_permissions(administrator = True)
  async def explosivedm(self,ctx, target: discord, amount=1, *,message):
    for _ in range(amount):
      await target.send(message)
  
  @commands.command()
  @commands.has_permissions(administrator = True)
  async def dm(self,ctx, target: discord.User, *,message):
    await target.send(message)
    
  @commands.Cog.listener()
  async def on_ready(self):
    print('moderation_commands has been loaded') 
    

def setup(client):
  client.add_cog(moderation(client))