import requests 
#import bs4
from bs4 import BeautifulSoup as BS

url = "https://finance.naver.com/item/sise_day.naver?code={}&page={}"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

def get_stock(code, s_page=1, e_page=None):
    global bs
    result = []
    for cnt1 in range(s_page, e_page+1):
        r = requests.get(url.format(code,cnt1), headers=head)
        bs = BS(r.text, 'lxml')
        rt = bs.find("table", {'class' :"type2"})
        for cnt2 in [2, 3, 4, 5,6, 10, 11, 12, 13, 14]:
            tmp = rt.findAll("tr")[cnt2]
            result.append([x.text.strip().replace(",", "") for x in tmp.findAll("td")] )
    return result

if __name__=="__main__":
    print(get_stock("005930", 1,3))