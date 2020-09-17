import requests
from bs4 import BeautifulSoup

# pagination hard-coded
for page in range(1, 51):
    # setup url
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'

    # store all the books information as a list
    books_list = []

    req = requests.get(url)

    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'html.parser')

        article = soup.find_all('article', class_='product_pod')


        for book in article:
            title = book.find_all('a')[1]['title']
            price = book.find('p', class_='price_color').text[2:]
            instock = book.find('p', class_='instock availability').text.strip()

            books = {
                'title': title,
                'price': price,
                'instock': instock,
            }

            books_list.append(books)

    print(books_list)