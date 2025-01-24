# Entrada principal do bot
import os

import discord
from commands import register_commands  # Função para registrar comandos separados
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Configuração de Intents
intents = discord.Intents.default()
intents.message_content = True  # Permite acesso ao conteúdo das mensagens
intents.members = True  # Permite acesso ao conteúdo relacionado aos membros

# Inicializando o bot com o prefixo "!"
bot = discord.ext.commands.Bot(command_prefix="!", intents=intents)


# Evento: Bot pronto
@bot.event
async def on_ready():
    register_commands(bot)  # Registra comandos de outros módulos
    synced = await bot.tree.sync()  # Sincroniza os comandos de barra com o Discord
    # synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID)) # Vincula o Bot a um servidor
    print(f"Bot foi conectado ao Discord como: {bot.user.name}!")
    print(f"Comandos sincronizados: {len(synced)}")


# Iniciando o bot
bot.run(TOKEN)
