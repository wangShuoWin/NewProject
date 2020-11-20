import os
import yagmail

class EmailSend(object):
    def QQemail(self):
        yag = yagmail.SMTP(user='w1339211817@qq.com',password='dwxxxoqwhflwjdeh',host='smtp.qq.com')
        subject ="用采前台组周报-王硕"
        contents = './用电主站部工作周报2020年_02用采前台组_王硕.xls'
        yag.send(to='w1339211817@qq.com',subject= subject, contents=contents)

    def WangYiEmail(self):
        yag = yagmail.SMTP(user='15861797687@163.com',password='HEQKZJYMCMSYXIXF',host='smtp.163.com')
        subject = '用采前台组周报-王硕'
        contents = './用电主站部工作周报2020年_02用采前台组_王硕.xls'
        yag.send(to='15861797687@163.com',subject=subject,contents=contents)


if __name__=='__main__':
    send = EmailSend()
    # send.QQemail()
    send.WangYiEmail()