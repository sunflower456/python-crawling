import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from string import punctuation
from eunjeon import Mecab

mecab = Mecab()

def count_word_freq(data) :
    _data = data.lower()

    for p in punctuation :
        _data = _data.replace(p, "")

    _data = _data.split()

    # 명사 추출
    # _data = mecab.nouns(_data)
    # 형태소 별로 나눠 추출
    # _data = mecab.morphs(_data)
    # 형태소 별로 나누고 품사 출력
    # _data = mecab.pos(_data)

    counter = Counter(_data)

    return counter

def create_word_cloud(data) :
    counter = count_word_freq(data)
    
    cloud = WordCloud(font_path = "NanumBarunGothic.ttf", background_color = "white")
    cloud.fit_words(counter)
    cloud.to_file('cloud.png')
    

def crawling(soup) :
    div = soup.find("div", class_= "_article_body_contents")
    result = div.get_text().replace('\n', '').replcae('// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}', '').replace('\t', '')
    return result

def main() :
    custom_header = {
        'user_agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.03683.103 Safari/537.36'
    }
    url = "https://news.naver.com/main/read.nhn?mode=LSD?mid-shm&sid1=104&oid=421&aid=0004611563"
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")

    text = crawling(soup)
    create_word_cloud(text)

if __name__ == "__main__" :
    main()
        