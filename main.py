from fastapi import FastAPI, HTTPException
from models import Game

app = FastAPI()

#games list
games = [
    Game(id=1, title="Space Adventure", genre="Action", max_players=4, rating=4.7),
    Game(id=2, title="Puzzle Mania", genre="Puzzle", max_players=1, rating=4.2),
    Game(id=3, title="Race Master", genre="Racing", max_players=8, rating=4.5),
    Game(id=4, title="Fantasy Quest", genre="RPG", max_players=6, rating=4.8),
    Game(id=5, title="Battle Arena", genre="Multiplayer", max_players=10, rating=4.6),
]

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/games")
def get_all_games():
    return games

@app.get("/games/{id}")
def get_game_by_id(id: int):
    for game in games:
        if game.id == id:
            return game
    raise HTTPException(status_code=404, detail="Game not found")

@app.post("/games", status_code=201)
def add_game(game: Game):
    games.append(game)
    return game

@app.put("/games/{id}")
def update_game(id: int, game: Game):
    for i, g in enumerate(games):
        if g.id == id:
            games[i] = game
            return game
    raise HTTPException(status_code=404, detail="Game not found")

@app.delete("/games/{id}", status_code=204)
def delete_game(id: int):
    for i, game in enumerate(games):
        if game.id == id:
            del games[i]
            return
    raise HTTPException(status_code=404, detail="Game not found")
