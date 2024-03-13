from pokedex import Pokedex
from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

PkDex = Pokedex(db)

types = ["Fighting"]
weakness = ["Fire"]
PkDex.getPokemonsByType(types)
PkDex.getPokemonByName("Bulbasaur")
PkDex.verificaEvolucao("Bulbasaur")
PkDex.findGrass()
PkDex.getPokemonsByWeakness(weakness)

#db.resetDatabase()