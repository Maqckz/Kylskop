import requests
import random
from dotenv import load_dotenv
import spoonacular as sp
import json
import os
load_dotenv()
from googlesearch import search

API_KEY = os.environ.get("API_TOKEN")
HEADER = {"Content-Type":'application/json'}
api = sp.API(API_KEY)

print()

def menu():
    print("[1] Gör sökning på recept ")
    print("[2] Ge mat skämt ")
    print("[0] Avsluta programmet ")

menu()
meny = int(input("Välj ett av alternativen "))


def sök():
    print("Länk till recept: ")
    for ii in ingredient.json():
        query1 = ii["title"]
        for i in search(query1, tld="com", num=1, stop=1, pause=2):
            print(i)


def val1():
    for i in ingredient.json():
        print(i["title"])


def val():
    if recept1 >= 1 and recept1 <= 10: 
        print("Recept: ")
        val1()
        print()
        sök()
    
    else:
        print("Felaktig input. Vänligen försök igen ") 

def joke():
    response = api.get_a_random_food_joke()
    data = response.json()
    print(data['text']) 
    

while meny != 0:
    if meny == 1:
        query = input('Mata in ingredienser, spearera ingredienser med ",", mellanslag eller ".". Se till att du skriver de önskade ingredienserna på engelska: ')
        recept = input("välj antal recept mellan (1 - 10) ")
        ingredient = requests.get('https://api.spoonacular.com/recipes/findByIngredients?ingredients=' + query + '&number=' + recept + '&apiKey=' + f'{API_KEY}', params=HEADER,) 
        recept1 = int(recept)
        antal = recept1 - 1
        query1 = (ingredient.json()[0]['title'])
        print()
        val()
        print()

            
    elif meny == 2:
        print()
        joke()
    
    elif meny > 2 and meny < 0:
        print()
        print("Fel input, välj något av dem givna alternativen ")

    print()
    menu()
    meny = int(input("Välj ett av alternativen "))

print("DU AVSLUTADE PROGRAMMET!")
