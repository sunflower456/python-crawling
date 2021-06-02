import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    div = soup.find("div", class_="text_area")
    result = div.text.replace('\n', '')
    return result

def get_href(soup):
    result = []
    div = soup.find("div", class_="w_news_list type_issue")

    for a in div.find_all("a", class_="news") :
        result.append("https://news.sbs.co.kr"+a["href"])

        return result


def main():
    list_href = []
    list_content = []

    url = "https://news.sbs.co.kr/news/newsflash.do?plink-GNB&cooper=SBSNEWS"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    list_href = get_href(soup)
    print(list_href)

    for url in list_href :
        href_req = requests.get(url)
        href_soup = BeautifulSoup(href_req.text, "html.parser")
        result = crawling(href_soup)
        list_content.append(result)

    print(list_content)


if __name__ == "__main__" :
    main()