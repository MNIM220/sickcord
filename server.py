import discord
from discord.ext import commands

TOKEN = 'Nzg4MDk3NzY2MTU3MDU4MDk4.X9ejPQ.TlKThHUPMc_2dYWiswfAj-ouK6I'
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
async def create_channel(ctx, username='Poop'):
    print("started babe")
    guild = ctx.guild
    sik_channel = await guild.create_voice_channel('SikChan')
    mover = None
    for user in guild.members:
        if user.name == username:
            mover = user
    if not mover:
        return
    await mover.move_to(sik_channel)
    await sik_channel.delete()


@bot.command(name='join')
async def joinvoice(ctx):
    # """Joins your voice channel"""
    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await bot.join_voice_channel(voice_channel)


bot.run(TOKEN)
