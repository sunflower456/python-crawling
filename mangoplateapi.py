from bs4 import BeautifulSoup
import requests
import json


custon_header = {
    'referer' : 'https://www.mangoplate.com/',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.03683.103 Safari/537.36'
}

def get_reviews(code) :
    comments = []

    url = f"https://stage.mangoplate.com/api/v5{code}/reviews.json?language-kor&device_uuid=V3QHS158623423404336051dDed&device_type=web&start_index=0&request_count=5&sort_by=2"
    req = requests.get(url, headers=custon_header)

    reviews = json.loads(req.text)
    for review in reviews :
        comment = review["comment"]
        text = comment["comment"]
        comments.append(text)

    return comments

def get_restaurants(name) :
    url = f"https://www.mangoplate.com/search/{name}"
    req = requests.get(url, headers = custon_header)
    soup = BeautifulSoup(req.text, "html.parser")
    restaurant_list = []

    rest = soup.find_all("div", class_="list-restaurant-item")
    for a in rest :
        temp = a.find("div", class_="info")
        href = temp.find("a")
        href = href["href"]
        title = temp.find("h2", class_="title").text.replace('\n', '').replace('\t', '').replace(' ', '')
        t = (title, href)
        restaurant_list.append(t)

    return restaurant_list

def main() :
    name = input("검색어를 입력하세요 : ")
    restaurant_list = get_restaurants(name)

    for r in restaurant_list :
        print(r[0])
        print(get_reviews(r[1]))
        print("="*30)
        print("\n"*2)

if __name__ == "__main__" :
    main()