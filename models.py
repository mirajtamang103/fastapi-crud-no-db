from pydantic import BaseModel

class Game(BaseModel):
    id: int
    title: str
    genre: str          # e.g., "Action", "Puzzle"
    max_players: int
    rating: float       # e.g., 4.5 out of 5
