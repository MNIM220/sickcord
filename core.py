import os


def active(func):
    async def wrapper(ctx, *args, **kwargs):
        if os.getenv("DISCORD_BOT_IS_ACTIVE") == "active":
            return await func(ctx, *args, **kwargs)
        else:
            try:
                await ctx.channel.send("This command is not active")
            except:
                pass

    return wrapper


async def sik_core(guild, username):
    sik_user = None
    for vc in guild.voice_channels:
        for user in vc.members:
            if user.name == username:
                sik_user = user
    if not sik_user:
        return
    sik_channel = await guild.create_voice_channel('SikChan')
    await sik_user.move_to(sik_channel)
    await sik_channel.delete()
