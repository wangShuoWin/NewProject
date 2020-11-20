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

import requests
import json

class Setting():
        url = 'http://192.168.176.32:26666/query/areaElecQuaStat'
        cookie = 'token=F21B6C38336D404B.6A24D1309D18829D5D0BB61D3CA6CD43.153E1735F14A2095978BDD15F516A12B61391992E909069B547634C049E860E80CF41C20B77D31CD.zdd.34101.%25E7%2588%25B8%25E7%2588%25B8.02.4.1.1.%25E5%25AE%2589%25E5%25BE%25BD%25E7%259C%2581%25E7%2594%25B5%25E5%258A%259B%25E5%2585%25AC%25E5%258F%25B8.02; dataCollectionToken=eyJ0eXAiOiJKc29uV2ViVG9rZW4iLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJvcmdUeXBlIjoiMDIiLCJvcmdOYW1lIjoi5a6J5b6955yB55S15Yqb5YWs5Y-4Iiwib3JnTm8iOiIzNDEwMSIsImFjY2Vzc0lwIjoiMS4xLjEuMSIsInJvbGVJZCI6IjEyODIyNzcyMzkwMTQwNzIzMiIsIm5hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJ1c2VyTmFtZSI6ImFkbWluIiwidXNlcklkIjoiMzIiLCJjdXJyTG9naW5JcCI6IjE5Mi4xNjguMTc2LjE2MSIsImV4cCI6MTYwNDQzMDAwMCwibmJmIjoxNjA0MzY5NzIzfQ.1jgVculKlhp6FWtbJrpV4Npdj7TAVkf1DhXYqTHR6BE; tokenType=bearer'
        sea_auth = 'bearer.eyJ0eXAiOiJKc29uV2ViVG9rZW4iLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJvcmdUeXBlIjoiMDIiLCJvcmdOYW1lIjoi5a6J5b6955yB55S15Yqb5YWs5Y-4Iiwib3JnTm8iOiIzNDEwMSIsImFjY2Vzc0lwIjoiMS4xLjEuMSIsInJvbGVJZCI6IjEyODIyNzcyMzkwMTQwNzIzMiIsIm5hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJ1c2VyTmFtZSI6ImFkbWluIiwidXNlcklkIjoiMzIiLCJjdXJyTG9naW5JcCI6IjE5Mi4xNjguMTc2LjE2MSIsImV4cCI6MTYwNDQzMDAwMCwibmJmIjoxNjA0MzY5NzIzfQ.1jgVculKlhp6FWtbJrpV4Npdj7TAVkf1DhXYqTHR6BE'
        token = 'eyJ0eXAiOiJKc29uV2ViVG9rZW4iLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpc3N1c2VyIiwiYXVkIjoiYXVkaWVuY2UiLCJvcmdUeXBlIjoiMDIiLCJvcmdOYW1lIjoi5a6J5b6955yB55S15Yqb5YWs5Y-4Iiwib3JnTm8iOiIzNDEwMSIsImFjY2Vzc0lwIjoiMS4xLjEuMSIsInJvbGVJZCI6IjEyODIyNzcyMzkwMTQwNzIzMiIsIm5hbWUiOiLns7vnu5_nrqHnkIblkZgiLCJ1c2VyTmFtZSI6ImFkbWluIiwidXNlcklkIjoiMzIiLCJjdXJyTG9naW5JcCI6IjE5Mi4xNjguMTc2LjE2MSIsImV4cCI6MTYwNDQzMDAwMCwibmJmIjoxNjA0MzY5NzIzfQ.1jgVculKlhp6FWtbJrpV4Npdj7TAVkf1DhXYqTHR6BE'
        headers = {
            'Content-Type': 'application/json',
            'Cookie':cookie,
            'Host': '192.168.176.32:26666',
            'Referer': 'http://192.168.176.32:19213/',
            'sea-auth':sea_auth,
            'token':token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
        }
        payload ={
        'orgNo': "34101",
            'orgType': "02",
            'statType': "day",
            'startTime': "2020-09-01",
            'endTime': "2020-10-31",
        }
        payload2 = {
        'orgNo': "34101",
            'orgType': "02",
            'statType': "month",
            'startTime': "2020-09",
            'endTime': "2020-10",
        }
        def Respone(self):
            url = self.url
            headers = self.headers
            jdata = json.dumps(self.payload)
            respone = requests.post(url, headers=headers, data=jdata)
            ret = respone.content.decode()
            r = json.loads(ret)
            print(r)

        def Respone01(self):
            url =self.url
            headers = self.headers
            jdata = json.dumps(self.payload)
            respone = requests.post(url,headers=headers,data=jdata)
            ret = respone.content.decode()
            r = json.loads(ret)
            r1 = r['msg']
            r2 = r['code']
            return r1,r2

        def Respone02(self):
            url =self.url
            headers = self.headers
            jdata = json.dumps(self.payload2)
            respone = requests.post(url,headers=headers,data=jdata)
            ret = respone.content.decode()
            r = json.loads(ret)
            r1 = r['msg']
            r2 = r['code']
            return r1, r2


if __name__ == '__main__':
    app = Setting()
    app.Respone()