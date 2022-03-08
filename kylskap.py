import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()
from googlesearch import search

API_KEY = os.environ.get("API_TOKEN")
HEADER = {"Content-Type":'application/json'}
print()
query = input("Mata in ingredienser med , emellan: ")
recept = input("välj antal recept mellan (1 - 10) ")

recept1 = int(recept)
antal = recept1 - 1

#if query == 

ingredient = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=' + query + '&number=' + recept + '&apiKey=' + f'{API_KEY}', params=HEADER,) 

def val():
    print("Recept: ")
    if recept1 == 1: 
        print(ingredient.json()[0]['title'])
    elif recept1 == 2:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 3:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 4:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 5:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[3]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 6:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[3]['title'])
        print(ingredient.json()[4]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 7:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[3]['title'])
        print(ingredient.json()[4]['title'])
        print(ingredient.json()[5]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 8:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[3]['title'])
        print(ingredient.json()[4]['title'])
        print(ingredient.json()[5]['title'])
        print(ingredient.json()[6]['title'])
        print(ingredient.json()[7]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 9:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[3]['title'])
        print(ingredient.json()[4]['title'])
        print(ingredient.json()[5]['title'])
        print(ingredient.json()[6]['title'])
        print(ingredient.json()[7]['title'])
        print(ingredient.json()[antal]['title'])
    elif recept1 == 10:
        print(ingredient.json()[0]['title'])
        print(ingredient.json()[1]['title'])
        print(ingredient.json()[2]['title'])
        print(ingredient.json()[3]['title'])
        print(ingredient.json()[4]['title'])
        print(ingredient.json()[5]['title'])
        print(ingredient.json()[6]['title'])
        print(ingredient.json()[7]['title'])
        print(ingredient.json()[8]['title'])
        print(ingredient.json()[antal]['title'])
    else:
        print("Finns inte, Felaktig input ")


def sök():
    query = (ingredient.json()[0]['title'])

    for i in search(query, tld="com", num=1, stop=1, pause=2):
        print("Länk till recept: ")
        print(i)



print()
val()
print()
sök()
