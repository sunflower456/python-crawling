import requests
from bs4 import BeautifulSoup

def get_href(soup) :
    result = []
    ul = soup.find("ul", class_="list_news")

    for span in ul.find_all("span", class_="tit") :
        result.append(span.find("a")['href'])

    return result


def main() :
    list_href = []

    url = "https://sports.donga.com/ent?p=1&c=02"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)

if __name__ == "__main__" :
    main()