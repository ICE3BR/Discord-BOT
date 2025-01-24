# Este arquivo contém comandos que exibem informações sobre produtos ou serviços disponíveis
import discord
from discord import app_commands


# Comando produto1
# Exibe informações sobre o curso Python completo
async def produto1_command(interaction):
    embed = discord.Embed(
        title="Curso Python - Completo",
        description=(
            "Neste curso você vai aprender programação em Python.\n"
            "Aprenda a criar jogos, sites, sistemas, aplicativos e muito mais."
        ),
        color=discord.Color.purple(),
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1330416676264742984/1330416733122461748/embed.png"
    )
    embed.set_footer(text="Todos os direitos reservados.")
    await interaction.response.send_message(embed=embed)


# Função para registrar comandos de produtos
def register_product_commands(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="produto1",
            description="Informações sobre o curso Python completo",
            callback=produto1_command,
        )
    )
