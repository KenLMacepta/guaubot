from discord.ext import commands
import os
from keep_alive import keep_alive
import discord

intents = discord.Intents(messages=True,
                          guilds=True,
                          reactions=True,
                          members=True)

token = open("token.txt").read()

bot = commands.Bot(command_prefix="g!", help_command=None)


@bot.command()
async def load(ctx, extension):
    admin = await bot.fetch_user(446065082107953153)

    if not ctx.author == admin: return print("ACCESO DENEGADO")
    try:
        bot.load_extension(f'cogs.{extension}')
        print("Load con éxito!")
    except:
        print("Ya esta loadeada")
        pass


@bot.command()
async def unload(ctx, extension):
    admin = await bot.fetch_user(446065082107953153)
    if not ctx.author == admin: return print("ACCESO DENEGADO")
    try:
        bot.unload_extension(f'cogs.{extension}')
        print("Unload con éxito!")
    except:
        print("Ya esta unloadeada")
        pass


@bot.command()
async def reload(ctx, extension):
    admin = await bot.fetch_user(446065082107953153)
    if not ctx.author == admin: return print("ACCESO DENEGADO")
    try:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        print("Reload con éxito!")
    except:
        bot.load_extension(f'cogs.{extension}')
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        print("Reload con éxito!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
bot.run(token)
