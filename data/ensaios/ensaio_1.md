Durante a parte 1 da APS demorei um pouco para escolher a API, porque queria uma que deixasse meu projeto mais interessate. No final eu 
desencanei porque não vai impactar o resto da APS. Então, escolhi uma que não tivesse problemas de atualização de tokens com grandes quantidades de requisições, 
mais focado em realizar a entrega. 

No código, me compliquei um pouco para identificar a primeira palavra do "message.content" mas depois decobri a função "message.content.startsWith("command")" 
que facilitou e limpou o código. Ainda estou em dúvida ser utilizei o regex de forma correta para filtrar os possíveis parâmetros da função run. 
