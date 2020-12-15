import os
import time

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = 'BooBooBooBooB'
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.command(name='siktir')
@commands.has_role('ADKIR')
async def sik_sik(ctx, *args):
    username = ' '.join(args)
    if not username:
        await sik_core(ctx.guild, ctx.author.name)
        await ctx.channel.send("Are you kidding? Gimme Username Mofo")
        return
    print("started babe")
    await sik_core(ctx.guild, username)


@bot.command(name='sikvote')
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
    sik_message = f'can we please sik this {username} **** ?'
    message = await ctx.channel.send(sik_message)
    await message.add_reaction("👍")
    await message.add_reaction("👎")

    vote_time = 5
    while vote_time >= 0:
        if vote_time == 0:
            await message.edit(content=sik_message + "\nVote time expired.")
            break
        await message.edit(content=sik_message + "\n" + str(vote_time) + " seconds left...")
        vote_time -= 1
        time.sleep(1)
    message = await ctx.fetch_message(message.id)
    for reaction in message.reactions:
        async for user in reaction.users():
            if ctx.me.id == user.id:
                continue
            if reaction.emoji == "👎":
                if user.name == username:
                    await ctx.channel.send('{1.emoji} {0}, Who asked you?.'.format(user.name, reaction))
                else:
                    await ctx.channel.send('{1.emoji} {0}, F***boi alert.'.format(user.name, reaction))
    if message.reactions[0].count > message.reactions[1].count:
        await sik_core(ctx.guild, username)
        await ctx.channel.send("SIKTIR\nVoted off ez")
    else:
        await ctx.channel.send("💀 💀 💀 Hmmm no disconnect for now\nbut its closer than what you think")


@bot.command(name='ultimate_sik')
async def ultimate_sik(ctx):
    for vc in ctx.guild.voice_channels:
        for user in vc.members:
            await sik_core(ctx.guild, user.name)
    await ctx.channel.send("All SIKTIR\nVoted off ez")


async def sik_core(guild, username):
    sik_user = None
    for user in guild.members:
        if user.name == username:
            sik_user = user
    if not sik_user:
        return
    sik_channel = await guild.create_voice_channel('SikChan')
    await sik_user.move_to(sik_channel)
    await sik_channel.delete()


@bot.command(name='join')
async def joinvoice(ctx):
    # """Joins your voice channel"""
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)


bot.run(TOKEN)
