from services import apiclients

# TODO add URL for list of valid categories
VALID_CATEGORIES = 'TODO'


class FamousQuotes(object):
    def __init__(self) -> None:
        pass

    async def showcategories(self):
        return VALID_CATEGORIES

    async def get(self, **kwargs):
        category = kwargs.get('category', None)
        api_ninjas_client = apiclients.ApiNinjasClient()

        quotes = await api_ninjas_client.get_quote(category=category)
        if quotes is None or len(quotes) < 1:
            # should never get hit if category is None
            raise ValueError(f'invalid category \'{category}\'')
        quote = quotes[0]
        quote_text = quote['quote']
        author = quote['author']
        return f'"{quote_text}" - {author}'
