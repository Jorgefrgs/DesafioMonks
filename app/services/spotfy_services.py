import os
import base64
from typing import List, Dict
import requests
from fastapi import APIRouter, HTTPException
from app.models.post_model import PostData
from collections import Counter

router = APIRouter()

def get_token(client_id: str, client_secret: str) -> str:
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    
    if result.status_code != 200:
        print(f"Failed to get token: {result.text}")
        result.raise_for_status()

    json_result = result.json()
    return json_result.get("access_token")

def get_auth_header(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}

def get_artist_data(token: str, artist_ids: List[str]) -> List[Dict]:
    base_url = "https://api.spotify.com/v1/artists/"
    headers = get_auth_header(token)
    artist_data = []

    for artist_id in artist_ids:
        url = f"{base_url}{artist_id}"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to get artist data for {artist_id}: {response.text}")
            response.raise_for_status()
        
        data = response.json()
        images = [image["url"] for image in data["images"]]

        artist_data.append({
            "name": data["name"],
            "followers": data["followers"]["total"],
            "popularity": data["popularity"],
            "genres": data["genres"],
            "images": images
        })
    return artist_data

def create_rankings(artist_data: List[Dict]):
    pop_artists = [artist for artist in artist_data if "pop" in artist["genres"]]
    pop_rankings = sorted(pop_artists, key=lambda x: x["followers"], reverse=True)

    genre_counter = Counter(genre for artist in artist_data for genre in artist["genres"])
    top_genres = [genre for genre, _ in genre_counter.most_common(5)]

    return pop_rankings, top_genres

@router.post("/rankings")
async def get_rankings():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

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
async def submit_data(data: PostData):
    url = "https://psel-solution-automation-cf-ubqz773kaq-uc.a.run.app?access_token=bC2lWA5c7mt1rSPR"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=data.dict())
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return {"mensagem": "Dados adicionados com sucesso"}
