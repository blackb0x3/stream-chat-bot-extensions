from services import apiclients


class Pokemon(object):
    def __init__(self) -> None:
        pass

    async def typeof(self, **kwargs):
        pokemon_name = kwargs.get('name')

        if pokemon_name is None or pokemon_name == '':
            raise ValueError('pokemon name not provided!')

        pokeapi_client = apiclients.PokeapiClient()

        pokemon = await pokeapi_client.get_pokemon(pokemon_name)
        return f'{pokemon_name} is a ' + ' '.join([poketype['type']['name'] for poketype in pokemon['types']]) + ' type.'
