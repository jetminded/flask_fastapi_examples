from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ---- Models ----
class Spell(BaseModel):
    name: str
    damage: int

class Character(BaseModel):
    id: int
    name: str
    class_type: str
    level: int
    spells: List[Spell] = []

# ---- In-memory storage ----
characters = []

# ---- Routes ----

@app.get("/")
def root():
    return {"message": "Welcome to DnD Library API"}

# Create a character
@app.post("/characters")
def create_character(character: Character):
    characters.append(character)
    return character

# Get all characters
@app.get("/characters")
def get_characters():
    return characters

# Get character by ID
@app.get("/characters/{char_id}")
def get_character(char_id: int):
    for char in characters:
        if char.id == char_id:
            return char
    raise HTTPException(status_code=404, detail="Character not found")

# Add spell to character
@app.post("/characters/{char_id}/spells")
def add_spell(char_id: int, spell: Spell):
    for char in characters:
        if char.id == char_id:
            char.spells.append(spell)
            return {"message": "Spell added", "character": char}
    raise HTTPException(status_code=404, detail="Character not found")