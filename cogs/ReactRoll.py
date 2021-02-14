import discord
from discord.ext import commands
import json

class ReactRole(commands.Cog):

  def __init__(self,client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('ReactRole is ready')

  @commands.Cog.listener()
  async def on_raw_reaction_add(self,payload):

    if payload.member.bot:
        pass

    else:
        with open('reactrole.json') as react_file:
            data = json.load(react_file)
            for x in data:
                if x['emoji'] == payload.emoji.name:
                    role = discord.utils.get(self.client.get_guild(
                        payload.guild_id).roles, id=x['role_id'])

                    await payload.member.add_roles(role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self,payload):

    with open('reactrole.json') as react_file:
        data = json.load(react_file)
        for x in data:
            if x['emoji'] == payload.emoji.name:
                role = discord.utils.get(self.client.get_guild(
                    payload.guild_id).roles, id=x['role_id'])

                
                await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)

  @commands.command()
  @commands.has_permissions(administrator=True, manage_roles=True)
  async def reactrole(self,ctx, emoji, role: discord.Role, *, message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name, 
        'role_id': role.id,
        'emoji': emoji,
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)


def setup(client):
  client.add_cog(ReactRole(client))
  