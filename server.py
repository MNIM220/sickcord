from command import *
import os


TOKEN = 'Nzg4MDk3NzY2MTU3MDU4MDk4.X9ejPQ.a4TgBzyh7MpRiI0Gh9TaBOMlCbg'
GUILD = 'BooBooBooBooB'
os.environ["DISCORD_BOT_IS_ACTIVE"] = "active"


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
