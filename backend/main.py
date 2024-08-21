from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = {"http://127.0.0.1:5500"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hola")
def saludos():
    return "saludos"

animes = [{
    "coverImageUrl": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx114129-RLgSuh6YbeYx.jpg",
    "title": "Gintama: THE FINAL",
    "genres": ["action", "comedy", "drama", "sci-fi"],
    "rating": 91,
    "kind": "Movie",
    "reviews": 38620,
    "season": "Winter 2021"
},{
    "coverImageUrl": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx124194-pWfBqp3GgjOx.jpg",
    "title": "Fruits Basket: The Final",
    "genres": ["comedy", "drama", "psychological"],
    "rating": 90,
    "kind": "TV Show",
    "reviews": 37891,
    "season": "Spring 2021"
},{
    "coverImageUrl": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx5114-KJTQz9AIm6Wk.jpg",
    "title": "Hagane no Renkinjutsushi: FULLMETAL ALCHEMIST",
    "genres": ["action", "adventure", "drama", "fantasy"],
    "rating": 89,
    "kind": "TV Show",
    "reviews": 34600,
    "season": "Spring 2009"
},{
    "coverImageUrl": "https://s4.anilist.co/file/anilistcdn/media/anime/cover/medium/bx21-YCDoj1EkAxFn.jpg",
    "title": "One Piece",
    "genres": ["adventure","action","drama","fantasy"],
    "rating": 100,
    "kind": "TV Show",
    "reviews": 100000,
    "season": "Spring 2024"
}]

class Anime(BaseModel):
    coverImageUrl: str
    title: str
    genres: List[str]
    rating: int
    kind: str
    reviews: int
    season: str

@app.get("/animes")
def list_animes():
    return animes

@app.post("/animes")
def create_anime(anime : Anime):
    animes.append(anime)    
    return animes