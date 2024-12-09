# pokemon_info.py
import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(pokemon):
   # Obtiene los datos del Pokémon de la API.
    pokemon = pokemon.strip().lower()
    
    try:
        response = requests.get(URL + pokemon)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError:
        return None  # No se encontró el Pokémon
    except requests.exceptions.RequestException:
        return None  # Error de conexión o problemas con la API

def get_pokemon_moves(data):
    moves = [move['move']['name'] for move in data['moves']]
    return moves

def get_pokemon_types(data):
    types = [type_['type']['name'] for type_ in data['types']]
    return types

def get_pokemon_stats(data):
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    return stats
