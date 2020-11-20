import requests
from parsel import Selector


url = 'https://www.17k.com/chapter/3238041/41613168.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

res = requests.get(url, headers=headers)
res.encoding = res.apparent_encoding
selector = Selector(res.text)

p_list = selector.css('div.p p::text').getall()

result = ''
for i in p_list:
    result += i

print(result)