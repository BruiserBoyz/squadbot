import os
import discord

# pip install discord.py
# pip install python-dotenv
# pip install pillow
# pip install cogs
from discord.ext import commands
from dotenv import load_dotenv

project_folder = os.path.expanduser('..')  # adjust as appropriate
# project_folder = os.path.expanduser('~/Code/BruiserBoyz')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
SECRET_KEY = os.getenv("CLIENT_ID")

# client = discord.Client()
# channel_id = 'DEFINE_ME'
# token = 'DEFINE_ME'
#
# client = discord.Client()
# channel = discord.Object(id=channel_id)

client = commands.Bot(command_prefix=".bb", case_insensitive=True)

# displays an online message when bot is online.
@client.event
async def on_ready():
    # print('I have become self aware...')
    # print('logged in as')
    # print(client.user.name)
    # print(client.user.id)
    # print('-----')
    await client.change_presence(activity=discord.Game(name="I am self-aware"))


# cog load commands
@client.command()
async def load(ctx, extension):
    """loads an extension eg. .load (extension)"""
    client.load_extension(f'cogs.{extension}')
    await ctx.send("The extension was loaded.")


# cog unload commands
@client.command()
async def unload(ctx, extension):
    """unloads an extension eg. .unload (extension)"""
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("The extension was unloaded.")


# cog reload commands
@client.command()
async def reload(ctx, extension):
    """reloads an extension eg .reload (extension) """
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("The extension was reloaded.")


# loads extensions (COGS) when on ready
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# Run it.
client.run(SECRET_KEY)
