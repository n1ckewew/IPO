from urllib.parse import urlunparse
sbor = ('https', 'grand-piece-online.fandom.com', '/wiki/Devil_Fruits', '', '', '')
# Собираем URL обратно в строку
url = urlunparse(sbor)
print(url)
