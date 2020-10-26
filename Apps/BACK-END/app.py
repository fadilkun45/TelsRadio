from flask import (Flask, redirect, url_for, request, render_template)
import requests
import bs4
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    url     = requests.get('https://winpoin.com/')
    soup    = bs4.BeautifulSoup(url.text,'html.parser')
    #BERITA 1
    post    = soup.find_all('div','item-details')[0].find('a').get_text()
    link    = soup.find_all('div','item-details')[0].find('a')['href']
    author = soup.find_all('div','td-module-meta-info')[0].find('span','td-post-date').get_text()
    deksripsi = soup.find_all('div','td-excerpt')[0].get_text()
    thumbnail = soup.find_all('div','td-module-thumb')[2].find('img')['src']
    #BERITA 2
    post_2    = soup.find_all('div','item-details')[1].find('a').get_text()
    link_2    = soup.find_all('div','item-details')[1].find('a')['href']
    author_2 = soup.find_all('div','td-module-meta-info')[1].find('span','td-post-date').get_text()
    deksripsi_2 = soup.find_all('div','td-excerpt')[1].get_text()
    thumbnail_2 = soup.find_all('div','td-module-thumb')[3].find('img')['src']
    #BERITA 3
    post_3    = soup.find_all('div','item-details')[2].find('a').get_text()
    link_3    = soup.find_all('div','item-details')[2].find('a')['href']
    author_3 = soup.find_all('div','td-module-meta-info')[2].find('span','td-post-date').get_text()
    deksripsi_3 = soup.find_all('div','td-excerpt')[2].get_text()
    thumbnail_3 = soup.find_all('div','td-module-thumb')[4].find('img')['src']

    return render_template('index.html', post=post, link=link,author=author,deskripsi=deksripsi,thumbnail=thumbnail,
                                         post_2=post_2,link_2=link_2,author_2=author_2,deskripsi_2=deksripsi_2,thumbnail_2=thumbnail_2,
                                         post_3=post_3,link_3=link_3,author_3=author_3,deskripsi_3=deksripsi_3,thumbnail_3=thumbnail_3)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

