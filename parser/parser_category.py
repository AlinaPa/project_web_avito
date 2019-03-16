def get_avito_ads():
	html = get_html("https://www.avito.ru/moskva/avtomobili?radius=0")
	if html:
		soup = BeautifulSoup(html, 'html.parser')
		all_ads = soup.find('div', class_='catalog-list').findAll('div', class_='item_table')
		print(all_ads)
		result_ads = []
		for ads in all_ads:
			title = ads.find('div', class_='item_table-header').find('h3', class_="title").text.strip()
			url = ads.find('a', class_='item-description-title-link')['href']
			price = ads.find('span', class_='price').text.strip()
			description = ads.find('div', class_='specific-params').text.strip()
			result_ads.append({
				"title": title,
				"url": url,
				"price": price,
				"description": description
			})
		return print(result_ads)
	return False

"""
if __name__ == "__main__":
	html = get_html("https://www.avito.ru/moskva/avtomobili?radius=0")
	if html:
		with open("avito_category.html", "w", encoding="utf8") as f:
			f.write(html)
"""
get_avito_ads()

