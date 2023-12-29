from urllib.parse import urlparse

url=urlparse ('//grand-piece-online.fandom.com/wiki/Devil_Fruits')
print(url)
url._replace(scheme='https')