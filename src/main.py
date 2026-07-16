import discord
from discord.ext import commands
from discord import app_commands

intents= discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name} - {bot.user.id}')

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

bot.run("YOUR_BOT_TOKEN")