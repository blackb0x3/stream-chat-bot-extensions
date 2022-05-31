from shared import helpers, enums
from typing import Union

import aiohttp
import os

API_NINJAS_DOMAIN = 'https://api.api-ninjas.com'
API_NINJAS_API_KEY_CONFIG_NAME = 'ApiNinjasApiKey'
API_NINJAS_API_KEY_HEADER_NAME = 'X-Api-Key'
QUOTES_ENDPOINT = '/v1/quotes'
POKEAPI_GET_POKEMON_ENDPOINT = '/api/v2/pokemon'


class ApiNinjasClient(object):
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession(base_url=API_NINJAS_DOMAIN)
        self.api_key = os.environ[API_NINJAS_API_KEY_CONFIG_NAME]

        if not self.api_key:
            raise KeyError('No entry for api key - api-ninjas.com')

    async def get_quote(self, category: Union[str, None] = None):
        query_params = dict()

        if not helpers.is_none_empty_or_whitespace(category):
            query_params['category'] = category

        headers = self._build_headers()

        async with self.session as sesh:
            async with sesh.get(QUOTES_ENDPOINT, headers=headers, params=query_params) as response:
                if response.status == enums.HttpStatusCode.OK.value:
                    return await response.json()
                else:
                    raise RuntimeError(response.text())

    def _build_headers(self):
        return {
            API_NINJAS_API_KEY_HEADER_NAME : self.api_key
        }


class PokeapiClient(object):
    def __init__(self) -> None:
        self.session = aiohttp.ClientSession(base_url='https://pokeapi.co')

    async def get_pokemon(self, name: str):
        async with self.session as sesh:
            async with sesh.get(f'{POKEAPI_GET_POKEMON_ENDPOINT}/{name}') as response:
                if response.status == enums.HttpStatusCode.OK.value:
                    return await response.json()
                else:
                    raise RuntimeError(response.text())
