import requests
import json

from requests.api import request

custon_header = {
    'referer' : 'http://finance.daum.net/quotes/A048410#home',
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.03683.103 Safari/537.36'
}

def get_data() :
    result = []
    url = "http://finance.daum.net/api/search/rank?limit=10"
    req = requests.get(url, headers=custon_header)

    if req.status_code == requests.codes.ok:
        print("접속 성공")
        stock_data = json.loads(req.text)

        for d in stock_data["data"] :
            result.append([d['rank'], d['name'], d['tradePrice']])
        
    else :
        print("접속 실패")

    return result

def main() :
    data = get_data()
    for d in data :
        print(d)

if __name__ == "__name__" :
    main()