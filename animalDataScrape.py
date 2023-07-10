import requests
from bs4 import BeautifulSoup

def clean_words(words):
    cleaned_words = []
    for word in words:
        if not any(char.isdigit() or char == '?' or char == '—' for char in word):
            cleaned_words.append(word)
    return cleaned_words

def print_animal_data_by_rules(table):
    for row in table.find_all("tr"):
        columns = row.find_all("td")
        if len(columns) >= 2:
            animal = columns[0].text.strip()
            collective_nouns = clean_words(columns[4].find_all(string=True))
            collateral_adjective = clean_words(columns[5].find_all(string=True))

            if len(collective_nouns) == 0 or collective_nouns[0] == "":
                print(f"{animal} - {' '.join(collateral_adjective)}")
            if len(collective_nouns) > 1:
                for noun in collective_nouns:
                    print(f"{animal} - {noun.strip()}")

def scrape_animal_data():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_animal_names")
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find_all("table", class_="wikitable")[1]
    print_animal_data_by_rules(table)

scrape_animal_data()
