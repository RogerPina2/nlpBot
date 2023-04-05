# nlpBot - APS da matéria NLP

Autor: Roger Pina 

## Introdução
Esse repositório contém minha APS (atividade prática supervisionada) da matéria NLP (Natural Language Processing) que consiste na construção de um chatBot para discord utilizando processamento de linguagem natural. 

## A APS

A APS foi dividida em partes, cada uma com rúbrica/avaliação e entregas definidas. 
- Parte 0: Um chatbot para o Discord.
- Parte 1: Chatbot faz pequenos queries em um serviço externo como mapa, clima, bolsa de valores, etc.
- Parte 2: Chatbot faz webscrapping, guarda bases de dados e responde a queries de busca.
- Parte 3: Chatbot filtra conteúdo inadequado e só responde usando páginas com sentimento positivo.
- Parte 4: Chatbot gera conteúdo à partir de sua base de dados.
- Parte 5: Chatbot integra com GPT-3.

O arquivo completo com as avaliações e entregas de cada parte pode ser encontrado no [aqui](https://github.com/tiagoft/NLP/blob/main/APS.md)

## Por que um chatBot usando NLP e porque para o discord?
Um resumo feito pelo próprio chatGPT:

- Criar um chatbot com NLP (Natural Language Processing) pode melhorar a experiência do usuário em diversos setores, oferecendo atendimento ao cliente personalizado e eficiente, além de automatizar tarefas repetitivas. Além disso, chatbots com NLP podem coletar dados e insights valiosos sobre o comportamento do usuário, mas requerem conhecimento técnico especializado em inteligência artificial, linguística e desenvolvimento de software.

A conversa inteira pode ser lida [aqui](chat_with_chatGPT.md)

Quanto ao uso do discord, é uma plataforma com chat que os alunos possuem grande proximidade e possui uma estrutura fácil de ser substituída para utilizar o bot em outras plataformas como o Twitter.  

## Como rodar

1. Clone o repositório
- `git clone https://github.com/RogerPina2/botNLP.git`

2. Tokens de acesso

- 2.1 Crie um arquivo `.env` na raiz do projeto 
- 2.2 Adicione ao arquivo criado os tokens de acesso do `discord` e da api `thecatapi`. 

Deve ficar assim:
```
DISCORD_TOKEN=token_do_bot
API_KEY=api_key_do_ipgeolocation
```

3. Instale as bibliotecas utilizadas pelo projeto
- `pip install -r requirements.txt`

4. Na raiz do projeto, inicie o **BOT**
- `python3 bot.py`

## Ensaios

Em cada ensaio explico como foi o processo de fazer o chatbot entre as entregas da APS;
- [Ensaio 0](data/ensaios/ensaio_0.md)
- [Ensaio_1](data/ensaios/ensaio_1.md)
> - [Ensaio_2](data/ensaios/ensaio_2.md)
> - [Ensaio_3](data/ensaios/ensaio_3.md)
> - [Ensaio_4](data/ensaios/ensaio_4.md)
> - [Ensaio_5](data/ensaios/ensaio_5.md)
