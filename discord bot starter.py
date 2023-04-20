import discord
from discord.ext import commands
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions
import datetime
from typing import List
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
clientprefix = '^'
BotRpc = "RPC"
client = commands.Bot(command_prefix=clientprefix, intents=intents,status=discord.Status.idle)

@client.event
async def on_ready():
    print('Bot working as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=BotRpc),status=discord.Status.do_not_disturb)
    print('rpc set! at ', str(datetime.datetime.now))
    print('Bot is now working! started at: ', str(datetime.datetime.now))
    print('--------------------------------------------------------------')

@client.command()
async def hello(ctx):
    ctx.reply("Hi!")

client.run('YOUR TOKEN GOES HERE')