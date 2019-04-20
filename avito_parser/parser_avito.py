import datetime
import requests
from bs4 import BeautifulSoup


from product.models import Product


def get_html(url):
	try:
		result = requests.get(url)
		result.raise_for_status()
		return result.text
	except(requests.RequestException, ValueError):
		print("Сетевая ошибка")
		return False


def save_products(title, url, price, metro):
	new_product = Product(title=title, url=url, price=price, metro=metro, created_at=datetime.datetime.now())
	new_product.save()


def get_avito_ads():
	html = get_html("https://www.avito.ru/moskva/odezhda_obuv_aksessuary/zhenskaya_odezhda/obuv")
	if html:
		soup = BeautifulSoup(html, 'lxml')
		all_ads = soup.find('div', class_='catalog-list')
		ads = all_ads.find_all('div', class_='item_table')
		result_ads = []
		for ad in ads:
			title = ad.find('div', class_='item_table-header').find('h3', class_="title").text.strip()
			url = ad.find('a', class_='item-description-title-link')['href']
			price = ad.find('span', class_='price').text.strip()
			metro = ad.find('div', class_='data').find_all('p')[-1].text.strip()
			save_products(title, url, price, metro)


get_avito_ads()

