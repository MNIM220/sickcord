import os
import redis


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


redis_client = None


def start_redis():
    host = os.getenv("REDIS_HOST")
    port = int(os.getenv("REDIS_PORT"))
    return redis.Redis(host=host, port=port, db=1)


def set_redis(key, value, expire, client):
    return client.set(key, value, ex=expire)


def get_redis(key, client):
    return str(client.get(key))


def get_ttl_redis(key, client):
    return client.ttl(key)
