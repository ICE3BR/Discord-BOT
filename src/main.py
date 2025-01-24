import asyncio
import os

import discord
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Permite acesso ao conteúdo das mensagens
intents.members = True  # Permite acesso ao conteúdo relacionado aos membros
bot = commands.Bot(
    command_prefix="!", intents=intents
)  # Prefixo para comandos ex: !ping


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot foi conectado ao Discord com sucesso como: {bot.user.name}")


# Função compartilhada || >Comando Ping
async def ping_response(latency, send_method):
    await send_method(f"Pong! Latência {latency}ms")


# Comando baseado em prefixo
@bot.command(name="ping", description="Verifica a latência!")
async def ping_prefix(ctx):
    latency = round(bot.latency * 1000, 2)
    await ping_response(latency, ctx.send)


# Comando de barra (slash command)
@bot.tree.command(name="ping", description="Verifica a latência!")
async def ping_slash(interaction: discord.Interaction):
    latency = round(bot.latency * 1000, 2)
    await ping_response(latency, interaction.response.send_message)


@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send(f"{member.mention} se juntou ao servidor.")
        bemvindo = discord.Embed(
            title="Bem-vindo ao servidor!",
            description=f"Olá {member.mention} seja bem vindo ao servidor **{guild.name}**!",
            color=discord.Color.purple(),
        )
        bemvindo.set_thumbnail(
            url=member.avatar.url if member.avatar else bot.user.avatar_url
        )
        await guild.system_channel.send(embed=bemvindo)


bot_commands = """
`!V6A` - Ver informações sobre nosso bot
`!ping` - Ver latência
`!clear` - Limpar mensagens
`!produto1` - Ver curso
`!ticket` - Abrir ticket
"""


@bot.command(name="V6A", description="Ver informações sobre nosso bot")
async def sobre(ctx):
    embed = discord.Embed(
        title="Sobre nosso bot",
        description=f"Sou um bot criado para ensinar programação no discord!",
        color=discord.Color.purple(),
    )

    embed.add_field(name="Comandos Disponiveis", value=bot_commands, inline=False)
    embed.set_footer(text="Criado por: ICE3BR")
    await ctx.send(embed=embed)


@bot.command(name="produto1")
async def produto1(ctx):
    embed = discord.Embed(
        title="Curso Python - Completo",
        description=f"Neste curso voce vai aprender programação em Python.\nAprenda a criar jogos, sites, sistemas, aplicativos e muito mais.",
        color=discord.Color.purple(),
    )

    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1330416676264742984/1330416733122461748/embed.png?ex=678de6a3&is=678c9523&hm=7655acdfc6caa6380647cf359f89cb0f8153edfb93ad563d4b953d272ff24c2d&"
    )  # 400x200px
    embed.set_footer(text="Todos os direitos reservados.")

    class Produto1View(View):
        @discord.ui.button(label="Comprar", style=discord.ButtonStyle.success)
        async def comprar_callback(
            self, interaction: discord.Interaction, button: discord.ui.Button
        ):
            await interaction.response.send_message(
                "Clique aqui para realizar sua compra: [Link de Compra](https://www.udemy.com/course/python-completo/)",
                ephemeral=True,
            )

    view = Produto1View()

    await ctx.send(embed=embed, view=view)


@bot.command(name="ticket")
async def ticket(ctx):
    embed = discord.Embed(
        title="Suporte - Ticket do Bot V6A",
        description="Clique no botão para abrir um ticket!",
        color=discord.Color.purple(),
    )
    embed.set_footer(text="Todos os direitos reservados.")
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1330416676264742984/1330416733122461748/embed.png"
    )

    class TicketView(View):
        @discord.ui.button(label="Abrir Ticket", style=discord.ButtonStyle.success)
        async def open_ticket(
            self,
            interaction: discord.Interaction,
            button: discord.ui.Button,
        ):
            guild = ctx.guild
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                ctx.author: discord.PermissionOverwrite(read_messages=True),
                guild.me: discord.PermissionOverwrite(read_messages=True),
            }

            # Criando o canal privado
            ticket_channel = await guild.create_text_channel(
                name=f"ticket-{ctx.author.name}", overwrites=overwrites
            )

            await ticket_channel.send(
                f"Bem-Vindo, {ctx.author.mention}!\nNosso suporte estará com você em breve!"
            )
            await interaction.response.send_message(
                "Seu ticket foi criado!\nVerifique o canal criado no servidor.",
                ephemeral=True,
            )

            # Adiciona botão para fechar o canal
            class CloseTicketView(View):
                @discord.ui.button(
                    label="Fechar Chat", style=discord.ButtonStyle.danger
                )
                async def close_ticket(
                    self, interaction: discord.Interaction, button: discord.ui.Button
                ):
                    # Envia a mensagem de aviso com o tempo restante
                    await interaction.response.send_message(
                        "O ticket será fechado e o canal excluído em 8 segundos.",
                        ephemeral=True,
                    )

                    # Aguarda 8 segundos antes de deletar o canal
                    await asyncio.sleep(5)

                    # Exclui o canal
                    await interaction.channel.delete(
                        reason="Ticket fechado pelo usuário"
                    )

            close_view = CloseTicketView()
            await ticket_channel.send(
                "Clique no botão abaixo para fechar este ticket.", view=close_view
            )

    view = TicketView()
    await ctx.send(embed=embed, view=view)


@bot.command(name="clear")
@commands.has_permissions(manage_messages=True)
async def clear_messages(ctx):
    # Envia uma mensagem de aviso
    await ctx.send("Limpando todas as mensagens do canal...")

    # Deleta todas as mensagens do canal, incluindo as mensagens enviadas pelo bot
    await ctx.channel.purge()

    # Envia uma mensagem temporária confirmando a limpeza
    confirmation_msg = await ctx.send("Todas as mensagens do canal foram apagadas!")
    await asyncio.sleep(4)  # Aguarda 4 segundos
    await confirmation_msg.delete()  # Exclui a mensagem de confirmação


@bot.command(name="volp")
async def msg_volp_mention(ctx):
    user_id = 705184112327131179  # Substitua pelo ID real do usuário
    mention = f"<@{user_id}> É o mais gostoso do Universo!!"
    await ctx.send(f"{mention}!")


bot.run(TOKEN)

# python src/main.py
