import discord
from discord.ext import commands
from time import sleep

class moderator(commands.Cog):

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
  async def spam(self,ctx,reps,*,content):
    for rep in range(reps):
      ctx.send(content)
      sleep(1)


  @commands.Cog.listener()
  async def on_ready(self):
    print('moderator_commands has been loaded') 

def setup(client):
  client.add_cog(moderator(client))