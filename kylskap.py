import requests
from configparser import ConfigParser
config = ConfigParser()
config.read('./config/config_keys.cfg')

API_KEY = config.get('spoonacular', 'api_key')

def getRecipeByIngredients(ingredients):
    payload = {
        'fillIngredients': False,
        'ingredients': ingredients,
        'limitLicense': False,
        'number': 5,
        'ranking': 1
    }

    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"


    headers={
        "X-Mashape-Key": API_KEY,
        "X-Mashape-Host": "mashape host"
    }

    r = requests.get(endpoint, params=payload, headers=headers)
    results = r.json()
    title = results[0]['title']
    print(title)

getRecipeByIngredients('apple') 