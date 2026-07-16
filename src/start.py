import discord

intents = discord.Itents.default()
intents.message_content = True

client = discod.Client(intents=intents)

@client.event
async def on_ready():
    print(f'logged in as {client.user.name} - {client.user.id}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("your token here")



## propieties 
## enable-query = true
## query.port = 25565


## enable-rcon = true
## rcon.port = 25575
## rcon.password = 676767