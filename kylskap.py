import requests
from dotenv import load_dotenv
import json
import os
load_dotenv()
from googlesearch import search

API_KEY = os.environ.get("API_TOKEN")
HEADER = {"Content-Type":'application/json'}
print()
query = input('Mata in ingredienser med "," som separerar(engelska): ')
recept = input("välj antal recept mellan (1 - 10) ")


recept1 = int(recept)
antal = recept1 - 1

#if query == 

ingredient = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=' + query + '&number=' + recept + '&apiKey=' + f'{API_KEY}', params=HEADER,) 

query1 = (ingredient.json()[0]['title'])

def sök():

    print("Länk till recept")
    for ii in ingredient.json():
        query1 = ii["title"]
        for i in search(query1, tld="com", num=1, stop=1, pause=2):
            print(i)


def val1():
    for i in ingredient.json():
        print(i["title"])



def val():
    print("Recept: ")
    if recept1 >= 1 and recept1 <= 10: 
        val1()
        print()
        sök()

    else:
        print("Finns inte, Felaktig input ")




print()
val()
print()
