import os
import random

import discord
from discord.ext import commands


def getToken():
    with open("env.txt") as tokenFile:
        return tokenFile.readline()


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def gif(ctx):
    folder = "gifs"
    randGif = random.choice(os.listdir(folder))
    await ctx.send(file=discord.File(f"{folder}\{randGif}"))


bot.run(getToken())