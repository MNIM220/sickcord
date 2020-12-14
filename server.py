import os
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
    print("started babe")
    await sik_core(ctx.guild, username)


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
