import os
import re

import discord
from dotenv import load_dotenv

from modules import crawler, searcher, wn_searcher
from modules.variables import *
from modules.api.catAPI.images import get_random_image

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name='Piratas do Klan')
    # channel1 = discord.utils.get(guild.text_channels, name='testebot')

    guild = discord.utils.get(client.guilds, name='A Cidade dos Robôs')
    #channel = discord.utils.get(guild.text_channels, name='bot-fest')
    #channel = discord.utils.get(guild.text_channels, name='bot-training')
    # await channel1.send('O bot está online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel):
        content = message.content.lower()

        if message.content.lower() == '!oi':
            user = message.author
            user = user.name.split('#')[0]
            await message.channel.send(f'Olá {user}! ')

        elif message.content.lower() == '!source':
            await message.channel.send('Este é o link do repositório do chatBot: https://github.com/RogerPina2/botNLP')

        elif message.content.lower() == '!author':
            await message.channel.send('O nome do autor do bot é: Roger Ribeiro Fava Pina, seu email é: rogerrfp@al.insper.edu.br')
        
        elif message.content.startswith('!help'):
            message_words = message.content.split(' ')
            
            if len(message_words) == 1:
                await message.channel.send(help_message)    

            elif len(message_words) == 2 and message_words[1] == 'oi':
                await message.channel.send('!oi : Retorna uma saudação do bot.')

            elif len(message_words) == 2 and message_words[1] == 'source':
                await message.channel.send('!source : Retorna o link do repositório do bot.')
            
            elif len(message_words) == 2 and message_words[1] == 'author':
                await message.channel.send('!author : Retorna o nome do criador do bot.')

            elif len(message_words) == 2 and message_words[1] == 'run':
                await message.channel.send('!run <pet> : Retorna uma imagem aleatória do pet. Pet pode ser "dog" ou "cat"')

        # Run
        elif message.content.startswith('!run'):
            message_words = message.content.split(' ')
            
            if len(message_words) == 1:
                await message.channel.send(run_missing_argument) 
            
            elif len(message_words) == 2:
                param = message_words[1]
                regex_pet = r'^(dog|cat)$'
                result = re.match(regex_pet, param)

                if result and param == 'cat':
                    await message.channel.send(get_random_image(pet='cat')[0]['url'])
                elif result and param == 'dog':
                    await message.channel.send(get_random_image(pet='dog')[0]['url'])
                else:
                    await message.channel.send(run_wrong_param)

            else:
                await message.channel.send('Essa função aceita apenas um parâmetro')

        # Crawl
        elif message.content.startswith('!crawl'):
            message_words = message.content.split(' ')
            
            if len(message_words) == 1:
                await message.channel.send(run_missing_argument) 
            
            elif len(message_words) == 2:
                param = message_words[1]
                regex_url = r"(https?://[^\s]+)"
                result = re.match(regex_url, param)

                if result:
                    res = crawler.crawl(param)
                    await message.channel.send(f'{res[0]} novos sites adicionados.') 
                
                else:
                    await message.channel.send(run_wrong_param)
                
            else:
                await message.channel.send('Essa função aceita apenas um parâmetro')

        # Search
        elif message.content.startswith('!search'):
            message_words = message.content.split(' ')
            
            if len(message_words) == 1:
                await message.channel.send(run_missing_argument) 
            
            else:
                _th = False
                if message_words[-1][:3] == 'th=':
                    _th = True
                    param = ' '.join(message_words[1:-1])
                    
                else:
                    param = ' '.join(message_words[1:])
                
                regex_url = r"\b\w+\b"
                result = re.match(regex_url, param)
                
                if result:
                    _th_value = 0
                    if _th:
                        _th_value = float(message_words[-1].split("=")[-1])

                    url = searcher.query(param.lower(), th=_th_value)[0]

                    if url:
                        await message.channel.send(url) 
                    else:
                        await message.channel.send('Query não encontrada.')

                else:
                    await message.channel.send(run_wrong_param)

        # Wn_search
        elif message.content.startswith('!search'):
            message_words = message.content.split(' ')
            
            if len(message_words) == 1:
                await message.channel.send(run_missing_argument) 
            
            elif len(message_words) == 2:
                param = message_words[1]
                regex_url = r"[A-Za-z0-9]\w*|[^\w\s]"
                result = re.match(regex_url, param)

                best_word, url = wn_searcher.wn_search(result.lower())

                if best_word is not None:
                    await message.channel.send(f'A melhor palavra encontrada foi: {best_word} e o link recomendado é: {url}')
                else:
                    await message.channel.send('Não foi encontrado palavra semelhante no dataset.')    
            else:
                await message.channel.send('Essa função aceita apenas um parâmetro')

    else:
        if message.content.lower() == '!oi':
            await message.channel.send('Olá em um canal público!')

discord_token = os.getenv('DISCORD_TOKEN')
client.run(discord_token)