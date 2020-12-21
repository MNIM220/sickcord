import os
import time
from random import randrange
import discord
from discord.ext import commands
from core import active, sik_core, start_redis, get_ttl_redis, set_redis

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

redis_conn = start_redis()


@bot.command(name='sik-help')
async def helper(ctx, *args):
    await ctx.channel.send("```!siktir <username>\n"
                           "!sikvote <username>\n"
                           "!ultimate_sik\n"
                           "!activate\n"
                           "!deactivate\n"
                           "!malme [multiplier] <username>\n```")


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
    await message.add_reaction("🕊")

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
            if reaction.emoji == "🕊":
                expire = get_ttl_redis(str(user.id), redis_conn)
                if expire <= 0:
                    if randrange(100) == 85:
                        await ctx.channel.send(
                            "😮😮😮😮😮😮😮😮😮😮\nOh My F\***en G\*d\nRandom is here\n{0} - Unluky Babe :)".format(
                                username))
                        break
                    set_redis(str(user.id), "temp", 3600, redis_conn)
                    await ctx.channel.send(
                        "malande alert\n{0} is a real malande\nyou cant veto for an hour\nVOTE AGAIN DONT WORRY".format(
                            user.name))
                    return
                else:
                    await ctx.channel.send('{0} - Veto on cool down Get F\****ed'.format(user.name))
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


@bot.command(name='malme')
@active
async def malme(ctx, *args):
    try:
        multiplier = int(args[0])
        if multiplier > 10:
            multiplier = 10
        for i in range(0, multiplier):
            await ctx.channel.send(' '.join(args[1:]))
    except:
        await ctx.channel.send(' '.join(args))


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
    if os.getenv("DISCORD_BOT_IS_ACTIVE") == "inactive":
        os.environ["DISCORD_BOT_IS_ACTIVE"] = "active"
        await ctx.channel.send("Activated")
    else:
        await ctx.channel.send("Are you siking with me?")


@bot.command(name='deactivate')
@commands.has_role('ADKIR')
async def deactivate_bot(ctx, *args):
    if os.getenv("DISCORD_BOT_IS_ACTIVE") == "active":
        os.environ["DISCORD_BOT_IS_ACTIVE"] = "inactive"
        await ctx.channel.send("Deactivated")
    else:
        await ctx.channel.send("Are you siking with me?")


@bot.command(name='shutdown')
@commands.has_role('ADKIR')
async def shutdown(ctx, *args):
    await bot.close()
