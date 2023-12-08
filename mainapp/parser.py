import opengrapher
from .models import BookMark






print(parse_and_save("https://ogp.me/#types"))

# from bs4 import BeautifulSoup
# import requests
#
#
# def og_parsing(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")
#     title = soup.find('meta', property="og:title")
#     title = title.get("content")
#     desc = soup.find('meta', property="og:description")
#     desc = desc.get("content")
#     url = soup.find('meta', property="og:url")
#     url = url.get("content")
#     wtype = soup.find('meta', property="og:type")
#     wtype = wtype.get("content")
#     # preview = soup.find('meta', property="og:image")
#     # preview = preview.get("content")
#     print(title)
#     print(desc)
#     print(url)
#     print(wtype)
#
#
# print(og_parsing("https://ogp.me/#types"))
