import requests
from bs4 import BeautifulSoup

def crawling(soup) :
    result = []
    ul = soup.find("ul", class_="list_news")

    for span in ul.find_all("span", class_="tit") :
        result.append(span.get_text())
    
    return result

def main() :
    answer = []
    url = "https://sports.donga.com/ent"

    for i in range(0,5) :
        req = requests.get(url, params = {'p':i*20+1})
        soup = BeautifulSoup(req.text, "html.parser")

        answer += crawling(soup)

        print(answer)

if __name__ == "__main__" :
    main()