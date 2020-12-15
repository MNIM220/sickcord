import os
import time

import discord
from discord.ext import commands
from core import active, sik_core

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='siktir')
@commands.has_role('ADKIR')
@active
async def sik_sik(ctx, *args):
    username = ' '.join(args)
    if not username:
        await sik_core(ctx.guild, ctx.author.name)
        await ctx.channel.send("Are you kidding? Gimme Username Mofo")
        return
    print("started babe")
    await sik_core(ctx.guild, username)


@bot.command(name='sikvote')
@active
async def sik_sik(ctx, *args):
    username = ' '.join(args)
    if not username:
        await sik_core(ctx.guild, ctx.author.name)
        await ctx.channel.send("Learn NooB\nNo username given so\nVoted off ez")
        return
    not_there = False
    for vc in ctx.guild.voice_channels:
        for user in vc.members:
            if username == user.name:
                not_there = True
    if not not_there:
        await sik_core(ctx.guild, ctx.author.name)
        await ctx.channel.send("She is not in Voice so\nVoted off ez")
        return
    sik_message = f'can we please sik this {username} \**** ?'
    message = await ctx.channel.send(sik_message)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

    vote_time = 10
    while vote_time >= 0:
        if vote_time == 0:
            await message.edit(content=sik_message + "\nVote time expired.")
            break
        await message.edit(content=sik_message + "\n" + str(vote_time) + " seconds left...")
        vote_time -= 1
        time.sleep(1)
    message = await ctx.fetch_message(message.id)
    boi_action = False
    for reaction in message.reactions:
        async for user in reaction.users():
            if ctx.me.id == user.id:
                continue
            if reaction.emoji == "👎":
                if user.name == username:
                    boi_action = True
                    await ctx.channel.send('{1.emoji} {0}, Who asked you?'.format(user.name, reaction))
                else:
                    await ctx.channel.send('{1.emoji} {0}, F***boi alert'.format(user.name, reaction))
    if boi_action:
        message.reactions[1].count = message.reactions[1].count - 1
    if message.reactions[0].count > message.reactions[1].count:
        await sik_core(ctx.guild, username)
        await ctx.channel.send("SIKTIR\nVoted off ez")
    else:
        await ctx.channel.send("💀 💀 💀 Hmmm no disconnect for now\nbut its closer than what you think")


@bot.command(name='ultimate_sik')
@commands.has_role('ADKIR')
@active
async def ultimate_sik(ctx, *args):
    for vc in ctx.guild.voice_channels:
        for user in vc.members:
            await sik_core(ctx.guild, user.name)
    await ctx.channel.send("All SIKTIR\nVoted off ez")


@bot.command(name='activate')
@commands.has_role('ADKIR')
async def activate_bot(ctx, *args):
    if os.getenv("DISCORD_BOT_IS_ACTIVE") == "deactive":
        os.environ["DISCORD_BOT_IS_ACTIVE"] = "active"
        await ctx.channel.send("Activated")
    else:
        await ctx.channel.send("Are you siking with me?")


@bot.command(name='deactivate')
@commands.has_role('ADKIR')
async def deactivate_bot(ctx, *args):
    if os.getenv("DISCORD_BOT_IS_ACTIVE") == "active":
        os.environ["DISCORD_BOT_IS_ACTIVE"] = "deactive"
        await ctx.channel.send("Deactivated")
    else:
        await ctx.channel.send("Are you siking with me?")
