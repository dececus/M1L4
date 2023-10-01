import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def emoji(ctx):
    elements = ["😀", "😇", "😎", "😛", "🗿", "🐀", "💵"]
    await ctx.send(random.choice(elements))

@bot.command()
async def cat(ctx):
    elements = ['cat1.jpg', 'cat2.jpg', 'cat3.jpg', 'cat4.jpg', 'cat5.jpg']
    await ctx.send(file=discord.File(random.choice(elements)))
    
@bot.command()
async def meme(ctx):
    elements = ['meme1.jpg', 'meme2.jpg', 'meme3.jpg', 'meme4.jpg', 'meme5.jpg']
    await ctx.send(file=discord.File(random.choice(elements)))

bot.run("MTE1NTUwMDI1ODMzMjI1MDIyMg.GAlEGt.mpQvOkQ1ZEQEz5Ug5MeXGPMRKtG5mYmph6Bin4")
