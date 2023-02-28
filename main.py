#pythonCopy code
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name='Piratas do Klan')
    channel = discord.utils.get(guild.text_channels, name='testebot')
    await channel.send('O bot está online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        if message.content.lower() == '!oi':
            await message.channel.send('Olá em mensagem privada!')

        elif message.content.lower() == '!source':
            await message.channel.send('Este é o link do repositório do chatBot: https://github.com/RogerPina2/botNLP')

        elif message.content.lower() == '!author':
            await message.channel.send('O nome do autor do bot é: Roger Ribeiro Fava Pina, seu email é: rogerrfp@al.insper.edu.br')

    else:
        if message.content.lower() == '!oi':
            await message.channel.send('Olá em um canal público!')

client.run('MTA3ODUwODg3NjMxMzQwMzQxMg.GhHY4j.1OpDPHsH5UvViJY7DCw9M-L2GfptPYVEZF-W1g')