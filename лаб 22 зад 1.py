import requests
import json

result = requests.get("https://swapi.dev/api/people/3/") # получение кода страницы методом get
if result.status_code == 200:
    json_dict = json.loads(result.text)  # десериализация JSON
    json_dict['name'] = input("Введите имя: ")
    with open("swap.json", "w") as file:
        json_text = json.dump(json_dict, file, indent=4)  #сериализация JSON
    # Доп:
    result_homeworld = requests.get(json_dict['homeworld'])
    print(result_homeworld.text)
