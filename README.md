# Buscar-passagens
Essa API é o resultado dos meus primeiros passos usando o Framework FastAPI.
Também uso no projeto conceitos de Web Crawler com Beautifulsoup.

# Documentação do projeto
[Documentação](https://buscar-passagens.herokuapp.com/docs#/default/tickets_tickets__get)

# Como usar o projeto?
Para acessar o serviço o usuário pode fazer uma requisição GET no endpoint [/tickets/](https://buscar-passagens.herokuapp.com/tickets) com os seguintes parâmetros:

## Parâmetros obrigatórios:
- from_city= Cidade de origem;
- from_state= Estado de origem;
- to_city= Cidade de destino;
- to_state= Estado de destino;

Se desejar refinar a busca, poderá passar os parâmetros opcionais:
- day= O dia da viagem;
- month= Mês da viagem;
- year= Ano da viagem.

# Qual é a origem dos dados?
Todos os dados exibidos na API são capturados por meio de um Cawler diretamente no site da https://www.clickbus.com.br/
Quando o usuário informa os dados para a busca, as passagens são recolhidas no site, de acordo com as informações,
e depois são retornadas como resposta da API
### Nenhum dado do usuário é armazenado, não é necessário informar nada sobre pagamento e nem dados de informações pessoais

# Ferramentas usadas para o desenvolvimento da API:
- Python 3.8.10;
- Fastapi 0.77.1
- Gunicorn 20.1.0
- Beautifulsoup4 4.11.1

# Ferramenta de hospedagem
- Heroku
