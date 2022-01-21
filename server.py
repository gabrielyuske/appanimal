from uuid import uuid4

from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel

app = FastAPI()

class Animal(BaseModel):
    id: Optional[int]
    nome : str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get("/")
def test():
    return {"test"}

# Objeto com todos os animais cadastrados
@app.get("/animais")
def lista_animais():
    return banco

# Obter dados de apenas do animal com id pedido
@app.get("/animais/{animal_id}")
def obter_animal(animal_id:str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
    return {"error":"ID nao esta cadastrado"}

@app.delete("/animais/{animal_id}")
def remover_animal(animal_id:str):
    posicao = -1
    #buscao posicao
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            posicao = index
            break
    if posicao != -1:
        banco.pop(posicao)
        return {"mensagem":"Animal removido"}
    else:
        return {"error":"ID nao esta cadastrado"}

# Envia os cadastro registrado dos animais
@app.post("/animais")
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None

