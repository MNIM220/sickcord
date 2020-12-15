from command import *
import os
from core import start_redis, set_redis, get_redis

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = 'BooBooBooBooB'
os.environ["DISCORD_BOT_IS_ACTIVE"] = "active"

_redis = start_redis()


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    guild_members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {guild_members}')


bot.run(TOKEN)
