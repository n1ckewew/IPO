import requests
import json

url = "https://swapi.dev/api/vehicles/4/"
# Отправляем запрос на сервер
result = requests.get(url)
# Проверяем успешность запроса
if result.status_code == 200:
    # Преобразуем полученные данные в JSON формат
    json_dict = json.loads(result.text)
    # Выводим информацию о стоимости песчаного гусеничного велосипеда
    print(f"Информация о песчаном гусеничном велосипеде:\n"
          f"Имя: {json_dict.get('name', 'Неизвестно')}\n"
          f"Стоимость: {json_dict.get('cost_in_credits', 'Неизвестно')} галактических кредитов")