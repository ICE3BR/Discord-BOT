# Entrada principal do bot
import os

import discord
from commands import register_commands
from discord.ext import commands
from dotenv import load_dotenv


class BotConfig:
    def __init__(self):
        # Carregando variáveis de ambiente
        load_dotenv()
        self.TOKEN = os.getenv("DISCORD_TOKEN")
        self.GUILD_ID = os.getenv("GUILD_ID")  # ID do servidor de desenvolvimento
        self.DEBUG_MODE = False  # Modo de Depuração (Altere para True para ligar)
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.intents.members = True
        self.bot = commands.Bot(
            command_prefix="!", intents=self.intents
        )  # Inicializando o bot
        self.add_prefix_commands()  # Adicionando comandos de prefixo (chamado após inicializar o bot)

    def set_activity(self, activity_type=1, name="Jogando Discord Bot V6A"):
        """
        Configura o status do bot baseado em um tipo e nome.
        :param activity_type: Tipo de atividade (1: Jogando, 2: Assistindo, 3: Ouvindo).
        :param name: Mensagem a ser exibida no status.
        """
        activity_types = {
            1: discord.ActivityType.playing,
            2: discord.ActivityType.watching,
            3: discord.ActivityType.listening,
        }
        activity = discord.Activity(
            type=activity_types.get(activity_type, discord.ActivityType.playing),
            name=name,
        )
        return activity

    async def on_ready(self):
        """
        Evento disparado quando o bot está pronto.
        """
        register_commands(self.bot)

        # Configurando o status simples
        activity = self.set_activity(
            activity_type=2, name="Vendo tudo o que você faz no Discord!"
        )
        await self.bot.change_presence(activity=activity)

        if self.DEBUG_MODE:
            # Exibir comandos registrados para depuração
            print("[DEBUG] Comandos registrados antes da sincronização:")
            for command in self.bot.tree.get_commands():
                print(f"- {command.name}: {command.description}")

            print(25 * "-")

            for guild in self.bot.guilds:
                print(f"Conectado ao servidor: {guild.name} (ID: {guild.id})")

        if self.DEBUG_MODE and self.GUILD_ID:
            # Registrar comandos para um servidor específico
            synced = await self.bot.tree.sync(
                guild=discord.Object(id=int(self.GUILD_ID))
            )
            print(
                f"[DEBUG] Comandos sincronizados para o servidor DEV: {len(synced)}"
            )  # Normalmente demora até 1h para sincronizar
        else:
            # Registrar comandos globalmente
            synced = await self.bot.tree.sync()
            print(
                f"Comandos sincronizados globalmente: {len(synced)}"
            )  # Normalmente demora até 1h para sincronizar

        if self.DEBUG_MODE:
            print("[DEBUG] Modo de Depuração está ativado")

        print(f"Bot foi conectado ao Discord como: {self.bot.user.name}!")

    def add_prefix_commands(self):
        """
        Adiciona comandos baseados em prefixo (!).
        """

        @self.bot.command(name="comandos")
        async def comandos_info(ctx):
            embed = discord.Embed(
                title="Aviso sobre os Comandos",
                description=(
                    "Este bot utiliza apenas **comandos de barra (/)**.\n"
                    f"Digite `/` ou `{self.bot.user.name}` no chat e explore as opções disponíveis!"
                ),
                color=discord.Color.orange(),
            )
            embed.set_footer(text="Obrigado por usar o bot!")
            await ctx.send(embed=embed)


# Instanciando e executando o bot
if __name__ == "__main__":
    config = BotConfig()

    # Adicionando o evento on_ready ao bot
    @config.bot.event
    async def on_ready():
        await config.on_ready()

    # Executando o bot
    config.bot.run(config.TOKEN)
