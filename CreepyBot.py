import discord
from discord.ext.commands import commands
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "$")
@client.event
async def on_ready():
    print("Thank you for turning me up master!")
    await client.change_presence(game=discord.Game(name="The prefix is $"))

@client.event
async def on_message(message):
    if message.content.startswith("hello"):
        msg = "Hello! (0.author.mention) How are you doing today?".format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith("bye"):
        msg = "Bye! (0.author.mention) i will see you later! (i hope)".format(message)
        await client.send_message(message.channel, msg)

client.run(os.getenv("BOT_TOKEN"))
    
