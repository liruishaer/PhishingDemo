#!/usr/bin/python2.7
#coding:utf-8
#如果想有中文注释就必须得有上面的语句
#File: myUtils.py
#Author: lxw

import smtplib
from email.message import Message
from Server import getServerEmail

def getRCB():
    recipient = raw_input("收件人: ")
    return recipient

def filterList(aList):
    length = len(aList)
    i = 0
    while i < len(aList):
        if aList[i] == "":
            del aList[i]
        else:
            i += 1
    return aList

def splitStr(string, sep):
    aList = string.split(sep)
    length = len(aList)
    for i in xrange(length):
        string = aList[i]
        string = string.strip()
        aList[i] = string
    return aList

def sendEmail(subject, content):
    """
    Send Email.
    """
    try:
        email, passwd, server = getServerEmail.getServerEmail()
        smtpServer = server
        userName = email
        password = passwd
        recipient = getRCB()
        rList = splitStr(recipient, ",")
        rList = filterList(rList)

        fromAddr = email
        toAddrs = rList #["lxwin@foxmail.com", "wangcuicui@cnnic.cn"]

        message = Message()
        message["Subject"] = subject
        message["From"] = fromAddr
        message["To"] = ";".join(toAddrs)
        #Copy to
        #message["CC"] is only for display, to send the email we must specify it in the method "SMTP.sendmail".
        #message["CC"] = "liuxiaowei@iscas.ac.cn,zhangyu2014@iscas.ac.cn,yunzhi@iscas.ac.cn"
        message["CC"] = "zhangyu2014@iscas.ac.cn,yunzhi@iscas.ac.cn"
        message.set_payload(content)
        message.set_charset("utf-8")
        msg = message.as_string()

        sm = smtplib.SMTP(smtpServer)
        sm.set_debuglevel(0)    #sm.set_debuglevel(1)
        sm.ehlo()
        sm.starttls()
        sm.ehlo()
        sm.login(userName, password)

        sm.sendmail(fromAddr, toAddrs, msg)
        sm.quit()
    except Exception, e:
        print "lxw Exception: ", e

def main():
    subject = raw_input("主题: ")
    content = raw_input("邮件内容: ")
    sendEmail(subject, content)
    print "邮件发送成功"

if __name__ == '__main__':
    main()


"""
14:30开会通知

下午跟我去怀柔雁栖湖校区开会，记得带上电脑和门禁卡！
"""
