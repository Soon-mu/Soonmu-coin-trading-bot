import requests
from bs4 import BeautifulSoup

def get_name(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#middle > .h_company > .wrap_company > h2 > a")
    tag = tags[0]
    return tag.text

def get_forignerShort(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html,"html5lib")
    tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > th > strong") #select 메서드는 조건에 만족하는 모든 태그를 파이썬 '리스트'로 반환한다
    tag = tags[0]
    return tag.text

def get_dividend(code):
    url = "https://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html,"html5lib")
    dvrs = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")
    dvr = dvrs[0]
    return dvr.text

print(get_name("012330") + "//" + get_forignerShort('012330') + " : " + get_dividend('012330'))