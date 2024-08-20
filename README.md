# Desafio Monks 👽
## FastAPI, React e Spotify Integration 🎵

<!-- Imagem ajustada -->
<img src="https://github.com/user-attachments/assets/d6b9a062-19e8-4c84-b511-98c9b0eefc3f" alt="Imagem 1" width="300"/>

<!-- Imagem ajustada -->
<img src="https://github.com/user-attachments/assets/271f5f28-0dfb-4ddb-989b-0993dd74d961" alt="Imagem 2" width="300"/>

<!-- Imagem ajustada -->
<img src="https://github.com/user-attachments/assets/042976f3-15b9-4d96-ab42-c950ae64eeb2" alt="Imagem 3" width="300"/>

<!-- Imagem ajustada -->
<img src="https://github.com/user-attachments/assets/2a121b80-9626-43dc-aac7-e45516ca3ad6" alt="Imagem 4" width="300"/>

<!-- Imagem ajustada -->
<img src="https://github.com/user-attachments/assets/16ff7abc-a0bb-49ba-8c94-75efe59bb12a" alt="Imagem 4" width="300"/>


# Requisitos e Setup 💻

## Instalação

### Para iniciar o projeto, siga os seguintes passos:
Clone o Repositório:

git clone https://github.com/Jorgefrgs/DesafioMonks.git

Inicie o Servidor:

cd .\DesafioMonks\

pip install fastapi pydantic requests uvicorn

uvicorn app.main:app --reload

cd .\DesafioMonks\front\spotfy-page\

npm install react

npm run dev


# Endpoints 📍

## 1. /rankings

Método: POST

Descrição: Obtém o ranking dos artistas pop e gêneros populares entre eles do Spotify.

Resposta:

![image](https://github.com/user-attachments/assets/d8b2c0fb-f912-4604-a691-061034f235a5)

![image](https://github.com/user-attachments/assets/3b3e1895-f9ab-48ed-9128-1840277e1e85)

Para testar: 127.0.0.1:5051/docs

Função get_token(client_id, client_secret): Obtém o token de acesso do Spotify.
Função get_artist_data(token, artist_ids): Obtém dados dos artistas com base nos IDs fornecidos.
Função create_rankings(artist_data): Cria e ordena os rankings de artistas e gêneros.

# 2. /submit ✅

Método: POST

Descrição: Envia os dados do projeto para um endpoint externo.

Parâmetros: Requer um corpo JSON com o formato específico.

## Corpo da Requisição:

json
{
  "github_url": "<Link do repositório do seu projeto>",
  "name": "<Seu nome>",
  "pop_ranking": [
    {
      "artist_name": "<Nome do artista>",
      "followers": "<Número de seguidores>"
    },
    ...
  ],
  "genre_ranking": [
    "<genre_1>",
    "<genre_2>",
    ...
  ]
}


A função submit_data chama o endpoint externo com os dados dos rankings.
Utiliza requests para enviar uma requisição POST com o cabeçalho e corpo apropriados.
CLIENT_ID e CLIENT_SECRET são necessários para a autenticação com o Spotify. Certifique-se de que esses valores estejam definidos corretamente.


FastAPI: Framework para criar APIs.

requests: Biblioteca para fazer requisições HTTP.

pydantic: Para validação de dados de entrada.

# Page 📄

![image](https://github.com/user-attachments/assets/409989cc-e2f9-405d-a2de-de1a3402be98)

![image](https://github.com/user-attachments/assets/156f539a-b659-420f-8cb6-e08251ac37dd)

