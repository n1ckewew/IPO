import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user agent': user}
link = 'https://brouser-info.ru/'
responce = requests.get(link).text
soup = BeautifulSoup(responce, 'lxml')
block = soup.find('div', id='tool_padding')
check_js = block.find('div', id='javascript_check')
result_js = check_js.find_all('span')[1].text
check_flash = block.find('div', id='flash_version')
status_flash = check_flash.find_all('span')[1].text
result_flash = f'flash: {status_flash}'
check_user = block.find('div', id='user_agent')
value_user = check_user.find('span').text
result_user = f'user agent: {value_user}'
print(result_js)
print(result_flash)
print(result_user)

find('a').get('href')
#проблемы с сайтом, просто переписать пример