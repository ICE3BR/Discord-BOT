# Comandos de diversão
import discord
from discord import app_commands


# Comando divertido: mencionar um usuário específico
async def volp_command(interaction: discord.Interaction):
    user_id = 705184112327131179  # Substitua pelo ID real do usuário
    mention = f"<@{user_id}> É a pessoa mais incrivel do Universo!!"
    await interaction.response.send_message(mention)


# Função para registrar comandos de diversão
def register_fun_commands(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="volp",
            description="Menciona uma pessoa especial com uma mensagem divertida",
            callback=volp_command,
        )
    )
