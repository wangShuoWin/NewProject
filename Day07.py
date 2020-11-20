import requests
import json
import re
from bs4 import BeautifulSoup
import os
import urllib
import urllib3

url='http://desk.zol.com.cn/37/'
respone = requests.get(url)
print(respone)
res = respone.content#.decode()
print(res)

#创建一个BeautifulSoup解析对象
soup = BeautifulSoup(res,'html.parser',from_encoding='utf-8')
#获取所有的链接
links = soup.find_all('img')
print('所有图片')

number = 1
try:
    for src in links:
        root = 'D://Python-Test//Image'
        path = root+'/'+ str(number) +'.jpg'
        if not os.path.exists(root):

            os.mkdir(root)
        if not os.path.exists(path):
            print(src['src'])
            r = requests.get(src['src'])
            print(r)
            with open(path, 'wb') as f:

                f.write(r.content)
                f.close()
                print("文件保存成功")
                number+=1
        else:
            print('保存失败')
except KeyError:
    print('KeyError')










