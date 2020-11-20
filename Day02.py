from random import randint
from tkinter import *
import json
import requests




def DoubleColor():
    import time
    time = time.strftime('%Y-%m-%d %H_%M_%S')
    url= 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=1'
    cookies= 'UniqueID=B88AWPnbaCqmUFpQ1603942257106; Sites=_21; 21_vq=1; _ga=GA1.3.749133244.1603942257; _gid=GA1.3.1213021565.1603942257; _gat_gtag_UA_113065506_1=1'

    headers={
        'cookie':cookies,
        'Referer': 'http://www.cwl.gov.cn/kjxx/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    respone = requests.get(url,headers=headers)
    print(respone)
    ret = respone.content.decode()
    r = json.loads(ret)
    r=r['result'][0]
    r1 = r['name']
    r2 = r['code']
    r3 = r['date']
    r4 = r['week']
    r5 = r['red']  #红球
    r6 = r['blue'] #蓝球
    r7 = r['content']
    s = [r1,r2,r3,r4,r5,r6,r7]
    s = str(s)
    print(s)

    with open('./log.txt','a+') as f:
            f.write(time + '\n'+ s)
            f.close()
    i=0
    j = []
    while  i<=5:
        num = str(randint(1,33))+','#红球
        i = i+1
        j.append(num)
    res.set(j)#获取红色球随机
    a = randint(1,16)#蓝球
    res2.set(a)#获取蓝色球随机
    res5.set(r2)#获取开奖期号
    res6.set(r3)#获取开奖日期
    res7.set(r4)#获取开奖日期
    res3.set(r5)  # 获取当前红球中奖号码
    res4.set(r6)  # 获取当前篮球中奖号码
    res8.set(r7)#获取中奖详情

master = Tk()
master.title('双色球')
master.geometry('340x170+300+300')

Label(master,text='脚本随机号码：',font=("黑体",18),fg='red').grid(row=2,column=0)
Label(master,text='实际开奖号码：',font=("黑体",18),fg='red').grid(row=3,column=0)
Label(master,text='开奖期号：',font=("黑体",10),fg='red').grid(row=4,column=0)
Label(master,text='开奖日期：',font=("黑体",10),fg='red').grid(row=5,column=0)
#Label(master,text='星期：',font=("黑体",10),fg='red').grid(row=6,column=0)
Label(master,text='中奖详情：',font=("黑体",10),fg='red').grid(row=7,column=0)



res = StringVar()
res2 = StringVar()
res3 = StringVar()
res4 = StringVar()
res5 = StringVar()
res6 = StringVar()
res7 = StringVar()
res8 = StringVar()

entry=Entry(master,textvariable=res,width=18,relief=RAISED) #红色球随机
entry.grid(row=2,column=1)

entry2 = Entry(master,textvariable=res2,width=3,relief=RAISED)#蓝色球随机
entry2.grid(row=2,column=3)

entry3 = Entry(master,textvariable=res3,width=18,relief=RAISED)
entry3.grid(row=3,column=1)

entry4 = Entry(master,textvariable=res4,width=3,relief=RAISED)
entry4.grid(row=3,column=3)

entry4 = Entry(master,textvariable=res5,width=15,relief=RAISED)
entry4.grid(row=4,column=1)

entry5 = Entry(master,textvariable=res6,width=15,relief=RAISED)
entry5.grid(row=5,column=1)

# entry6 = Entry(master,textvariable=res7,width=15,relief=RAISED)
# entry6.grid(row=6,column=1)

entry7 = Entry(master,textvariable=res8,width=15,relief=RAISED)
entry7.grid(row=7,column=1)

Button(master,text='查询',command=DoubleColor,width=15).grid(row=8,column=0)
Button(master,text='退出',command=master.quit,width=15).grid(row=8,column=1)

master.mainloop()



