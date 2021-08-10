from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

shazoo = "https://shazoo.ru/tags/419/games"
hinews = 'https://hi-news.ru/technology'
igr = "https://www.igromania.ru/news/"

shazoo_list = []
hinews_list = []
igr_list = []


def get_shazoo():
    r = requests.get(shazoo).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('h2', class_='entryTitle')
    for post in posts:
        title = post.find("a").text
        url = post.find('a').get('href')
        data = {'title': title,
                'url': url}
        shazoo_list.append(data)





def get_hinews():
    r = requests.get(hinews).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('h2', class_='post__title post__title_preview')
    for post in posts:
        title = post.find('a').text
        url = post.find('a').get('href')
        data = {'title': title,
                'url': url}
        hinews_list.append(data)


def get_igr():
    r = requests.get(igr).text
    soup = BeautifulSoup(r, 'lxml')
    posts = soup.find_all('div', class_='aubli_data')
    for post in posts:
        title = post.find('a', class_='aubli_name').text
        url = "https://www.igromania.ru/"+ post.find('a').get('href')
        data = {'title': title,
                'url': url}
        igr_list.append(data)


get_shazoo()
get_hinews()
get_igr()

def home(requests):
    context = {
        'shazoo_list': shazoo_list,
        'hinews_list': hinews_list,
        'igr_list': igr_list,
    }
    return render(requests, 'news_app/home.html', context)
