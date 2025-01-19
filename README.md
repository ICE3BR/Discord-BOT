# Bot de Discord - V6A

## Descrição

Este projeto é um bot de Discord criado com a biblioteca `discord.py`. O bot oferece funcionalidades como resposta a comandos, gerenciamento de tickets, envio de mensagens e embeds, além de ferramentas para limpar mensagens do canal.

## Estrutura do Projeto

```
.
├── .env                # Token do bot e variáveis de ambiente
├── .gitignore          # Arquivos e pastas ignorados pelo Git
├── LICENSE             # Licença do projeto
├── README.md           # Documentação do projeto
├── hello.py            # Arquivo de teste ou exemplo
├── pyproject.toml      # Configuração do ambiente Python
├── uv.lock             # Lockfile gerado pelo gerenciador de pacotes
├── src/                # Código principal do bot
│   ├── main.py         # Código principal do bot
├── services/           # Serviços auxiliares (em desenvolvimento)
├── tests/              # Testes do projeto
└── utils/              # Funções ou ferramentas auxiliares
```

## Funcionalidades

### 1. **Ping**
- Comando: `!ping`
- Retorna a latência do bot em milissegundos.

### 2. **Mensagem de Boas-Vindas**
- O bot envia uma mensagem de boas-vindas personalizada para novos membros.

### 3. **Sobre o Bot**
- Comando: `!sobre`
- Envia um embed com informações sobre o bot e seus comandos disponíveis.

### 4. **Produto Promocional**
- Comando: `!produto1`
- Envia um embed com informações sobre um curso e um botão de compra.

### 5. **Sistema de Tickets**
- Comando: `!ticket`
- Cria um canal de suporte privado e permite fechá-lo com um botão.

### 6. **Limpeza de Mensagens**
- Comando: `!clear`
- Remove todas as mensagens do canal (requer permissão de `Manage Messages`).

## Instalação

### Requisitos
- Python 3.8 ou superior
- Biblioteca `discord.py`
- Biblioteca `python-dotenv`

### Passos
1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   ```

2. Instale as dependências usando o `UV`:
   ```bash
   uv sync
   ```

3. Configure o arquivo `.env`:
   ```env
   DISCORD_TOKEN=seu_token_aqui
   ```

4. Execute o bot:
   ```bash
   python src/main.py
   ```

## Como Usar

1. Inicie o bot no servidor Discord configurado.
2. Use os comandos:
   - `!ping` para verificar a latência.
   - `!sobre` para informações sobre o bot.
   - `!produto1` para informações promocionais.
   - `!ticket` para abrir um canal de suporte.
   - `!clear` para limpar mensagens do canal (requer permissão).

## Melhorias Futuras

- Adicionar logs de atividades e tickets criados/fechados.
- Suporte a banco de dados para armazenar informações de tickets.
- Implementar novos comandos interativos.

