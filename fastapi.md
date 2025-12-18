Here is the **complete, simple step-by-step process** from **creating a venv** → **installing FastAPI** → **running the app**.

---

# ✅ **FULL PROCESS: Create venv → Install → Run FastAPI**

## **1. Create your project folder**

```powershell
mkdir fastapi
cd fastapi
```

---

## **2. Create a virtual environment**

```powershell
python -m venv venv
```

---

## **3. Activate the venv**

```powershell
.\venv\Scripts\activate
```

Your terminal should now show:

```
(venv) PS C:\Users\Miraj\...>
```

---

## **4. Install FastAPI + Uvicorn + CLI**

```powershell
pip install "fastapi[standard]"
```

This installs:

* FastAPI
* fastapi-cli → gives you the `fastapi dev` command
* Uvicorn
* Dependencies

---

## **5. Create your FastAPI app**

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}
```

---

## **6. Run the server**

### ✔ Option A — Using FastAPI CLI (recommended)

```powershell
fastapi dev main.py
```

### ✔ Option B — Using Uvicorn directly

```powershell
uvicorn main:app --reload
```

---

# ⭐ Your API will run at:

```
http://127.0.0.1:8000
```

Interactive docs:

```
http://127.0.0.1:8000/docs
```

---

Yes ✅ — the `.gitignore` file should be placed **inside your `fastapi/` folder**, i.e., the **root of your project** where `main.py`, `models.py`, and `requirements.txt` live.

Your folder structure would look like this:

```
fastapi/
│
├── .gitignore
├── main.py
├── models.py
├── requirements.txt
├── __pycache__/
├── .vscode/
└── venv/
```

---



### 💡 Why here?

* `.gitignore` affects **all files and folders in the same directory and below**.
* Placing it in `fastapi/` ensures Git ignores `__pycache__`, `venv`, `.vscode`, etc., **without affecting other projects on your machine**.

---

If you want, I can **give you a ready-to-use `.gitignore` specifically tuned for your FastAPI project structure**, optimized for GitHub.

Do you want me to do that?


If you want, I can generate a full starter project structure for you.
Got it! You want a `.gitignore` for a **FastAPI project** with your folder structure:

* Root: `main.py`, `models.py`, `requirements.txt`
* Subfolders: `__pycache__`, `.vscode`, `venv`

Here’s a proper `.gitignore` for that setup:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Virtual environment
venv/
ENV/
env/
.venv/

# VSCode settings
.vscode/

# MacOS
.DS_Store

# Logs
*.log

# Python packaging
*.egg-info/
dist/
build/

# IDEs
.idea/

# Pipenv
Pipfile.lock

# Coverage
.coverage
htmlcov/
*.cover

# Pytest cache
.pytest_cache/

# mypy cache
.mypy_cache/

# Ignore local database files if any (optional)
*.sqlite3
```

---

### ✅ Notes for your project

* `__pycache__/` → caches Python bytecode
* `.vscode/` → IDE-specific settings
* `venv/` → your virtual environment
* Keeps your repo **clean and lightweight**

---

If you want, I can also **write a complete folder structure with `.gitignore` ready to push to GitHub**, including `main.py`, `models.py`, and `requirements.txt`.

Do you want me to do that?


models.py

```python
from pydantic import BaseModel

class Game(BaseModel):
    id: int
    title: str
    genre: str          # e.g., "Action", "Puzzle"
    max_players: int
    rating: float       # e.g., 4.5 out of 5


    # Pydantic automatically generates an __init__ for you based on the fields (id, title, etc.).
    # def __init__(self, id :int, title: str, genre: str, max_players: int, rating: float):
    #     self.id = id
    #     self.title = title
    #     self.genre = genre
    #     self.max_players = max_players
    #     self.rating = rating
```

main.py

```python
from fastapi import FastAPI
from models import Game

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# List of games
games = [
    Game(id=1, title="Space Adventure", genre="Action", max_players=4, rating=4.7),
    Game(id=2, title="Puzzle Mania", genre="Puzzle", max_players=1, rating=4.2),
    Game(id=3, title="Race Master", genre="Racing", max_players=8, rating=4.5),
    Game(id=4, title="Fantasy Quest", genre="RPG", max_players=6, rating=4.8),
    Game(id=5, title="Battle Arena", genre="Multiplayer", max_players=10, rating=4.6),
]


@app.get("/games")
def get_all_games():
    return games

@app.get("/games/{id}")
def get_games_by_id(id: int):
    for game in games:
        if game.id == id:
            return game
    return "Game not found"

@app.post("/games")
def add_game(game: Game):
    games.append(game)
    return game

@app.put("/games")
def update_game(id: int, game: Game):
    for i in range(len(games)):
        if games[i].id == id:
            games[i] = game
            return "Game added successfully"
    return "Game not found"


@app.delete("/games")
def delete_game(id: int):
    for i in range(len(games)):
        if games[i].id == id:
            del games[i]
            return "Game deleted"
    return "Game not found"
```

Here is your **new `main.py` exactly as-is**, clean and correct ✅

```python
from fastapi import FastAPI, HTTPException
from models import Game

app = FastAPI()

# games list
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
```

✔ RESTful
✔ Proper status codes
✔ Clean routing
✔ Ready to run

If you want the **next upgrade** (auto ID, validation, database, routers), just say 👍

