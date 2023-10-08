import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents = discord.Intents.default())

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
    img_name = random.choice(os.listdir('cat'))
    with open(f'cat/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def memec(ctx):
    img_name = random.choice(os.listdir('meme_cat'))
    with open(f'meme_cat/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memep(ctx):
    img_name = random.choice(os.listdir('meme_prog'))
    with open(f'meme_prog/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("MTE1NTUwMDI1ODMzMjI1MDIyMg.GDjndA.wZJ3VX7WQTfgHodIpg_Z9Ag1ZjOpu1MXKFpa20")
