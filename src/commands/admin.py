# Comandos administrativos
import asyncio

import discord
from discord import app_commands
from discord.ext import commands


# Comando clear
# Limpa todas as mensagens do canal
@commands.has_permissions(manage_messages=True)
async def clear_command(interaction: discord.Interaction):
    # Envia uma mensagem de aviso
    await interaction.response.send_message(
        "Limpando todas as mensagens do canal...", ephemeral=True
    )

    # Deleta todas as mensagens do canal
    await interaction.channel.purge()

    # Envia uma mensagem temporária confirmando a limpeza
    confirmation_msg = await interaction.channel.send(
        "Todas as mensagens do canal foram apagadas!"
    )
    await asyncio.sleep(4)  # Aguarda 4 segundos
    await confirmation_msg.delete()  # Exclui a mensagem de confirmação


# Função para registrar comandos administrativos
def register_admin_commands(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="clear",
            description="Limpa todas as mensagens do canal atual",
            callback=clear_command,
        )
    )
