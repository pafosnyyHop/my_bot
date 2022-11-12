import requests
from bs4 import BeautifulSoup

ID_FILE_PATH = '/home/hello/Рабочий стол/telega_bot/id.txt' 
url = 'https://kaktus.media/'
def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text

def get_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    catatlog = soup.find('div', class_='Main')
    link = catatlog.find('div', class_='Main--all_news')
    link = link.find('a', class_ = 'Main--all_news-link').get('href')
    # print(link)
    
    return link



def get_all_news():
    html = get_html(url)
    link = get_link(html)
    link_ = get_html(link)
    links = []
    soup = BeautifulSoup(link_, 'html.parser')
    div = soup.find('div', class_='Tag--articles')
    div = div.find_all('div', class_='Tag--article')
    int_ = 1
    for x in div:
        div_ = x.find('div', class_= 'ArticleItem--data ArticleItem--data--withImage')
        all_news = div_.find('a', class_='ArticleItem--name').get('href')
        links.append(all_news)
        int_ += 1
        if int_ == 21:
            break
    return links

def get_page_data(link):
    html = get_html(link)
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find('div', class_ = 'Article')
    div = news.find('div', class_ = 'Article--block')
    div = div.find('div', class_ = 'Article--text')
    div_ = div.find('div', class_ = 'BbCode')
    news = [tag.text for tag in div_.find_all('p')]
    str_news = ' '.join(news)
    return str_news


def get_news_image() -> list:
    data = []
    html = get_html(url)
    link = get_link(html)
    link_ = get_html(link)
    soup = BeautifulSoup(link_, 'html.parser')
    div = soup.find('div', class_='Tag--articles')
    div = div.find_all('div', class_='Tag--article')
    int_ = 1
    for x in div:
        div_ = x.find('div', class_= 'ArticleItem--data ArticleItem--data--withImage')
        div = div_.find('a', class_='ArticleItem--name').text
        image_ = div_.find('a', class_='ArticleItem--image')
        image = image_.find('img', class_ = 'ArticleItem--image-img lazyload').get('src')
        link = div_.find('a', class_='ArticleItem--name').get('href')
        all_news = get_page_data(link)
        news = {
            'id': str(int_),
            'news': f'ID: {str(int_)}\n' + div,
            'image': image,
            'Description': all_news
        }
        data.append(news)
        int_ += 1
        if int_ == 21:
            break
    return data
 

    



def main():
    html = get_html(url)
    get_link(html)
    return get_news_image()




