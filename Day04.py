# a = [1,2,34,5,7]
# b = [1,2,34,5,7]
# c = [22,33,44,55,66]
# k =1
# l =2
# o=0
# p = 0
# for i in a:
#     for j in b:
#
#         if i == j:
#             print('i:'+str(i)+'j:'+str(j))
#             o=o+1
#             break
#
# if k == l:
#     print('deng')
#     p = p+1
#
# print(p)
# print(o)
#
# #题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# #1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去
# #掉不满足条件的排列。
# a = ''
# b = []
# for i in [1,2,3,4]:
#     for j in  [1,2,3,4]:
#         for k in  [1,2,3,4]:
#             if i!=j and i!=k and j != k:
#                print(i,j,k)
#https://www.iqiyi.com/v_19rr7plcfw.html?vfrm=pcw_home&vfrmblk=L&vfrmrst=712211_dianying_image2  八百

import requests
import json
from multiprocessing import Pool
from selenium import webdriver
import time
from tkinter import *


def run():
    a = str(entry.get())

    urls = 'https://660e.com/?url=' + a
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 隐藏提示语
    driver = webdriver.Chrome(options=options)
    driver.get(urls)
    res.set(urls)

master = Tk()
master.title('Vip视频解析')
master.geometry('500x100+300+300')

Label(master,text='Input url:',font=('宋体',15),fg='black').grid(row=0,column=0)
Label(master,text='Action url:',font=('宋体',15),fg='black').grid(row=1,column=0)

entry =Entry(master,width=50,relief=RAISED,highlightcolor='pink')
entry.grid(row=0,column=1)
res = StringVar()

entry2 = Entry(master,textvariable=res,width=50,relief=RAISED).grid(row=1,column=1)


Button(master,text='Action',command=run,width=15).grid(row=2,column=0)
Button(master,text = 'Exit',command=master.quit,width = 15).grid(row=2,column=1)

master.mainloop()




