import bs4
import requests


def main():
    authors = set()
    index = 1

    site_url = 'http://quotes.toscrape.com/page/'
    page_url = site_url + str(index)
    res = requests.get(page_url)

    while 'next' in res.text:
        page_url = site_url + str(index)
        res = requests.get(page_url)
        soup = bs4.BeautifulSoup(res.text, "lxml")

        for name in soup.select('.author'):
            authors.add(name.text)
        index += 1
    print(authors)


if __name__ == '__main__':
    main()
