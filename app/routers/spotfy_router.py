
import requests
from fastapi import APIRouter, HTTPException, Depends
from app.models.post_model import PostData
from app.services.spotfy_services import get_token, get_artist_data, create_rankings

router = APIRouter()


@router.post("/rankings")
async def get_rankings():
    client_id= "c8336bb12c47484fa782901457077174"
    client_secret= "91b49c3bddb2404584a8554be861dc42"

    if not client_id or not client_secret:
        raise HTTPException(status_code=500, detail="CLIENT_ID e CLIENT_SECRET não encontrados.")

    token = get_token(client_id, client_secret)

    artist_ids = [
        "6eUKZXaKkcviH0Ku9w2n3V", "1dfeR4HaWDbWqFHLkxsg1d", "66CXWjxzNUsdJxJ2JdwvnR",
        "04gDigrS5kc9YWfZHwBETP", "53XhwfbYqKCa1cC15pYq2q", "7dGJo4pcD2V6oG8kP0tJRR",
        "1HY2Jd0NmPuamShAr6KMms", "4gzpq5DPGxSnKTe4SA8HAU", "6vWDO969PvNqNYHIOW5v0m",
        "0du5cEVh5yTK9QJze8zA0C", "5pKCCKE2ajJHZ9KAiaK11H", "0EmeFodog0BfCgMzAIvKQp",
        "1uNFoZAHBGtllmzznpCI3s", "6S2OmqARrzebs0tKUEyXyp", "06HL4z0CvFAxyc27GXpf02"
    ]

    artist_data = get_artist_data(token, artist_ids)
    pop_rankings, genre_rankings = create_rankings(artist_data)

    return {"pop_ranking": pop_rankings, "genre_ranking": genre_rankings}


@router.post("/submit")
async def submit_data(rankings: dict = Depends(get_rankings)):
    pop_rankings = rankings["pop_ranking"]
    genre_rankings = rankings["genre_ranking"]

    post_data = {
        "github_url": "https://github.com/Jorgefrgs/DesafioMonks.git",
        "name": "Jorge Ferreira",
        "pop_ranking": [
            {"artist_name": artist["name"], "followers": artist["followers"]}
            for artist in pop_rankings
        ],
        "genre_ranking": genre_rankings
    }

    url = "https://psel-solution-automation-cf-ubqz773kaq-uc.a.run.app?access_token=bC2lWA5c7mt1rSPR"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=post_data)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return {"mensagem": "Dados adicionados com sucesso"}