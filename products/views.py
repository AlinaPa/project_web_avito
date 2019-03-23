from werkzeug.contrib.jsrouting import render_template

from pars.avito_category_parser import get_products


def index():
    title = "Название товара"
    url = "Ссылка на товар"
    product_list = get_products()
    return render_template('index', page_title=title, url=url, product_list=product_list)
