import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
import os

url = "https://www.amazon.com/EVGA-Optimized-Interlaced-Graphics-11G-P4-6393-KR/dp/B06Y11DFZ3/ref=sr_1_1?s=pc&ie=UTF8&qid=1531319504&sr=1-1&keywords=1080ti"
header = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
head_row = ['url','price','date']
today = date.today()
filename = 'results.csv'

request = requests.get(url, headers=header).text
soup = BeautifulSoup(request, 'html.parser')
price = soup.find(id='priceblock_ourprice').text
print(price)

with open(filename, 'a', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [url, price, today.strftime("%d/%m/%y")]
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        a.writerows([data])
    else:
        a.writerows([head_row, data])

