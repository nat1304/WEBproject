import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')  # ссылка + количество страниц
    total_pages = pages.split('=')[1]  #количество страниц

    return int(total_pages)  # Возвращает количество страниц

def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         data['district'],
                         data['url']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    adse = soup.find('div', class_='catalog-list')
    ads=soup.find_all('div', class_='item_table') # Всего объявлений на странице. ad - обявление; ads - список объявлений

    for ad in ads:
        try:
            title = ad.find('div', class_='description').find('h3').text.strip() # Показывает заголовок объявления
        except:
            title = ''  # Если заголовка нет, то поле остаётся пустое
        try:
            url = 'https://avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href') # Показывает ссылку на объявление
        except:
            url = ''
        try:
            price = ad.find('div', class_='about').text.strip() # Показывает цену
        except:
            price = ''
        try:
            district = ad.find('div', class_='data').find_all('p')[-1].text.strip() # Показывает станцию метро
        except:
            district = ''

        data = {'title': title,
                'price': price,
                'district': district,
                'url': url}
        write_csv(data)


def main():
    url = 'https://www.avito.ru/perm/tovary_dlya_kompyutera/fleshki_i_karty_pamyati?p=1'
    base_url = 'https://www.avito.ru/perm/tovary_dlya_kompyutera/fleshki_i_karty_pamyati?'
    page_part = 'p='

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i)
        print (url_gen)
        html = get_html(url_gen)
        get_page_data(html)

if __name__ == '__main__':
    main()
