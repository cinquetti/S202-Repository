from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, databases):
        self.database = databases

    def getPokemonByName(self, name: str):
        # Realiza a query para encontrar um Pokémon pelo nome
        result = self.database.collection.find({"name": name})
        # Escreve um log
        writeAJson(result, f"{name}")


    def getPokemonsByType(self, types: list):
        result = self.database.collection.find({"type": {"$in": types}})
        #Escreve um log
        writeAJson(result, "pokemonTipo")

    def findGrass(self):
        # Realiza a primeira query no banco de dados
        result = self.database.collection.find({"type": "Grass"})
        # Escreve um log
        writeAJson(result, "VerificaGrama")

    def verificaEvolucao(self, name: str):
        # Realiza a terceira query no banco de dados
        result = self.database.collection.find({"name": name, "next_evolution": {"$exists": True} })
        # Escreve um log
        writeAJson(result, f"verificaEvolucao{name}")

    def getPokemonsByWeakness(self, weakness: list):
        result = self.database.collection.find({"weaknesses": {"$in": weakness}})
        #Escreve um log
        writeAJson(result, f"verificaFraqueza")

