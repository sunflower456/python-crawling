import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    result = []

    ul = soup.find("ul", class_="rvw_list_area")
    for li in ul.find_all("li") :
        result.append(li.find("strong").get_text())

    return result

def get_href(soup) :
    ul = soup.find("ul", class_="search_list_1")
    href = ul.find("a")["href"].replace('basic', 'review')
    href = "https://movie.naver.com" + href

    return href

def get_url(movie) :
    return f"https://movie.naver.com/movie/search/result.nhn?query={movie}&section=all&ie=utf8"


def main() :
    list_href = []

    custom_header = {
        'referer' : 'https://www.naver.com',
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0 3683.103 Safari/537.36'

    }

    movie = input('영화 제목을 입력하세요.\n >')

    url = get_url(movie)

    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    movie_url = get_href(soup)

    href_req = requests.get(movie_url)
    href_soup = BeautifulSoup(href_req.text, "html.parser")

    list_href = crawling(href_soup)
    print(list_href)

if __name__ == "__main__" :
    main()