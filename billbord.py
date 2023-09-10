import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.m3rnfrd.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

URL = "https://www.billboard-japan.com/charts/detail?a=hot100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

print(soup)

musics = soup.select('#content2 > div > div.leftBox > table > tbody > tr')

for music in musics:
    banner = music.select_one('.exbanner')
    if banner:
        ''
    else:
        rank = music.select_one('td > span').text
        title = music.select_one('p.musuc_title').text.strip()
        artist = music.select_one('p.artist_name').text.strip()
        print(rank, title, artist)