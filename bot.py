import discord
from key import token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = token.get('TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} está online!')

@client.event
async def on_message(message):

    conteudo = message.content
    l_conteudo = conteudo.lower()

    if message.author == client.user:
        return

    if l_conteudo.startswith('!oi'):
        await message.channel.send(f'Oi {message.author}, tudo bem?')

@client.event
async  def on_message(message):

    conteudo = message.content
    l_conteudo = conteudo.lower()

    if message.author == client.user:
        return

    if l_conteudo.startswith('!ajuda'):
        await  message.channel.send(f'Olá {message.author.id}, um momento que iremos lhe ajudar!')

client.run(TOKEN)