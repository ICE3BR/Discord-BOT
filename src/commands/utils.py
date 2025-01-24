# Comandos utilitários
import asyncio

import discord
from discord import app_commands
from discord.ui import Button, View


# Comando ping
# Verifica a latência do bot
async def ping_command(interaction):
    latency = round(interaction.client.latency * 1000, 2)
    await interaction.response.send_message(f"Pong! Latência {latency}ms")


# Comando sobre
# Exibe informações sobre o bot
async def sobre_command(interaction):
    embed = discord.Embed(
        title="Sobre nosso bot",
        description="Sou um bot criado para ensinar programação no Discord!",
        color=discord.Color.purple(),
    )
    embed.add_field(name="Criador", value="ICE3BR", inline=False)
    await interaction.response.send_message(embed=embed)


# Comando ticket
# Abre um sistema de ticket para suporte
async def ticket_command(interaction):
    embed = discord.Embed(
        title="Suporte - Ticket do Bot V6A",
        description="Clique no botão para abrir um ticket!",
        color=discord.Color.purple(),
    )
    embed.set_footer(text="Todos os direitos reservados.")
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1330416676264742984/1330416733122461748/embed.png"
    )

    # View para interação com botões
    class TicketView(View):
        @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.success)
        async def open_ticket(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            guild = interaction.guild
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                interaction.user: discord.PermissionOverwrite(read_messages=True),
                guild.me: discord.PermissionOverwrite(read_messages=True),
            }

            # Criando o canal privado
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{interaction.user.name}", overwrites=overwrites
            )

            await ticket_channel.send(
                f"Bem-Vindo, {interaction.user.mention}!\nNosso suporte estará com você em breve!"
            )
            await interaction.response.send_message(
                "Seu ticket foi criado!\nVerifique o canal criado no servidor.",
                ephemeral=True,
            )

            # View para fechar o ticket
            class CloseTicketView(View):
                @discord.ui.button(
                    label="Fechar Chat", style=discord.ButtonStyle.danger
                )
                async def close_ticket(
                    self, interaction: discord.Interaction, button: discord.ui.Button
                ):
                    await interaction.response.send_message(
                        "O ticket será fechado e o canal excluído em 8 segundos.",
                        ephemeral=True,
                    )
                    await asyncio.sleep(8)
                    await interaction.channel.delete(
                        reason="Ticket fechado pelo usuário"
                    )

            close_view = CloseTicketView()
            await ticket_channel.send(
                "Clique no botão abaixo para fechar este ticket.", view=close_view
            )

    view = TicketView()
    await interaction.response.send_message(embed=embed, view=view)


# Função para registrar comandos utilitários
def register_util_commands(bot):
    bot.tree.add_command(
        app_commands.Command(
            name="ping", description="Verifica a latência!", callback=ping_command
        )
    )
    bot.tree.add_command(
        app_commands.Command(
            name="sobre", description="Informações sobre o bot", callback=sobre_command
        )
    )
    bot.tree.add_command(
        app_commands.Command(
            name="ticket",
            description="Abre um ticket de suporte",
            callback=ticket_command,
        )
    )
