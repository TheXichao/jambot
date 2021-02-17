import asyncio

import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.qualified_name} has been loaded')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)
        if reason is None:
            return await ctx.send(f'{member} has been kicked.')

        await ctx.send(f'{member} has been kicked for {reason}.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)
        if reason is None:
            return await ctx.send(f'{member.mention} has been banned.')

        await ctx.send(f'{member.mention} has been banned for {reason}.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: int):
        await ctx.guild.unban(discord.Object(id=user))
        await ctx.send(f'User has been unbanned.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def spam(self, ctx, repetitions=3, *, message):
        for _ in range(int(repetitions)):
            await ctx.send(message)
            await asyncio.sleep(1)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
        print(f'{ctx.author} cleared {amount} messages')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def explosivedm(self, ctx, target: commands.UserConverter, amount=1, *, message):
        for _ in range(amount):
            await target.send(message)
            await asyncio.sleep(1)

    @commands.command(aliases=['spamDM'])
    @commands.has_permissions(administrator=True)
    async def dm(self, ctx, target: commands.UserConverter, *, message):
        await target.send(message)


def setup(client):
    client.add_cog(moderation(client))
