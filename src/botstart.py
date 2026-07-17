import discord
from discord.ext import commands
from mcstatus import JavaServer
from mcrcon import MCRcon

TOKEN_DISCORD = 
IP_SERVIDOR =
PORTA_QUERY =
PORTA_RCON = 
SENHA_RCON = '676767'

## Inicialização do bot

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'bot{bot.user.name}conectado e pronto!')

## Status do McStatus e Query

@bot.command(name='status')
async def status_servidor(ctx):
    try: ##tenta conectar a query
        server = JavaServer.lookup(f'{IP_SERVIDOR}:{PORTA_QUERY}')
        status = server.status()

        mensagem = (
            f"🟢**Servidor Online!** \n"
            f"**Jogadores** {status.players.online}/{status.players.max}\n"
            f"**ping: ** {round(status.latency)}ms \n"
            f"**versão: ** {status.version.name}"
        )
        await ctx.send(mensagem)
    except Exception as e:
        await ctx.send("🔴Servidor offline ou inacessível no momento.")

## mensagem da RCON
    @bot.command(name='fala')
    async def send_message(ctx, *, message: str):
        if not ctx.author.guild_permissions.admin:
            await ctx.send("Você não tem permissão para usar isso.")
        
        try:
            with MCRcon(IP_SERVIDOR, SENHA_RCON, port=PORTA_RCON) as mcr:
                resposta = mcr.command(f"say [Duscird - {ctx.author.name}] {mensagem}")
                await ctx.send(f"Mensagem enviada pro servidor: `{mensagem}`")
        except Exception as e:
            await ctx.send(f"Erro ao conectar ao RCON: {e}")

bot.run(TOKEN_DISCORD)