# simple bot in python made by me :)

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='bot.log', encoding='utf-8', mode='w')
intents = discord.Intents.all()
intents.message_content = True
intents.members = True
intents.voice_states = True
intents.emojis = True
intents.messages = True
                        # where you see the "!" under this comment its how to start a command 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"im {bot.user.name} and im online :)")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
# just type hello
    if "hello" in message.content.lower():
        await message.channel.send(f"{message.author.mention} - how are you doing?")

    await bot.process_commands(message)

# !shh
@bot.command()
async def shh(ctx):
    await ctx.send(f"https://files.catbox.moe/nruc6r.png")

# !dm
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"you said {msg}")

# !ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"# why")
    await ctx.send(f"{message.author.mention}")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

