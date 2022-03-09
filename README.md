
# Kylskop
Denna README är skriven i markdown. Syftet med mitt projekt är att man ska mata in råvaror/ingredienser i programmet och få ut recept. Programmet är skrivet i Python och lite javascript.

# Teknologier/språk


# Usage 

Jag använder mig av ett ramverk som heter spoonacular. Det är en API för mat och därför perfekt för mitt program. När du skapar ett konto får du en API nyckel som ger dig tillgång till deras data. Det mitt program gör är att den tar en input som den sedan kör genom API:n och på så sätt får recept. Programmet tar ingredienserna som lagts in och letar efter recept som innehåller dessa på spoonaculars data. 

Sedan använder jag google-search för att ge länkar till recepten. Google-search tar titeln på receptet och söker på på det genom google. 

Jag har gjort en simpel meny för att göra navigation simpelt. 

```python
def menu():
    print("[1] Gör sökning på recept ")
    print("[2] Ge mat skämt ")
    print("[0] Avsluta programmet ")

menu()
meny = int(input("Välj ett av alternativen "))

```

Sedan har jag gjort funktioner för det man väljer och kallar funktionerna ifall man väljer något av alternativen.

```python
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
    
    elif meny > 2:
        print()
        print("Fel input, välj något av dem givna alternativen ")

    print()
    menu()
    meny = int(input("Välj ett av alternativen "))
```
Funktionerna:

```python
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
```
# Installation 

Kör följande kommandon för att installera det jag använder.

```cmd
pip install config
pip install python-dotenv
pip install googlesearch-python
```

Mina imports:

```python
import requests
import random
from dotenv import load_dotenv
import spoonacular as sp
import json
import os
load_dotenv()
from googlesearch import search
```


## To do
    - ~~Fixa meny~~
    - ~~Få recept av ingredienser~~
    - ~~Få mat skämt~~
    - Felhantering

# Contribution 
Pull request är tillåtet. Vid stora förändringar önskar jag att en issue öppnas för diskussion om ändringarna. Att fixa felhantering hade varit en stor hjälp för programmet.
