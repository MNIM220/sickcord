import os

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = 'BooBooBooBooB'
is_active = True

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
from command import *


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


bot.run(TOKEN)
