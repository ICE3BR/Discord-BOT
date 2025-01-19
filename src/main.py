import os

import discord
from discord.ext import commands
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
    print(f"Bot foi conectado ao Discord com sucesso como: {bot.user.name}")


@bot.command(name="ping")  #!hello
async def hello(ctx):
    latency = round(bot.latency * 1000, 2)
    await ctx.send(f"Pong! Latência {latency}ms")


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


@bot.command(name="sobre")
async def sobre(ctx):
    embed = discord.Embed(
        title="Sobre nosso bot",
        description=f"Sou um bot criado para ensinar programação no discord!",
        color=discord.Color.purple(),
    )

    embed.add_field(
        name="Comandos Disponiveis", value="`!ping`\n`!sobre`", inline=False
    )
    embed.set_footer(text="Criado por: ICE3BR")
    await ctx.send(embed=embed)


@bot.command(name="produto1")
async def produto1(ctx):
    embed = discord.Embed(
        title="Curso Python - Completo",
        description=f"Neste curso voce vai aprender programação em Python.\nAprenda a criar jogos, sites, sistemas, aplicativos e muito mais.",
        color=discord.Color.purple(),
    )

    embed.add_field(
        name="Link:", value="https://www.udemy.com/course/python-completo/", inline=True
    )
    embed.set_image(
        url="https://cdn.discordapp.com/attachments/1330416676264742984/1330416733122461748/embed.png?ex=678de6a3&is=678c9523&hm=7655acdfc6caa6380647cf359f89cb0f8153edfb93ad563d4b953d272ff24c2d&"
    )  # 400x200px
    embed.set_footer(text="Todos os direitos reservados.")
    await ctx.send(embed=embed)


bot.run(TOKEN)
