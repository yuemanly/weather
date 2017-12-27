#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-
# Name:        SMS
# Purpose:
#
# Author:      liusheng03
#
# Created:     19/12/2017
# Copyright:   (c) liusheng03 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from twilio.rest import Client

f = open('D:\git\pythonlearning\weather\SMS\data.txt')
lines = f.readlines()
f.close()
weather0 = str(lines[0])
weather1 = str(lines[1])
weather2 = str(lines[2])
weather = "%s %s %s" %(weather0.decode('cp936').encode('utf-8'),weather1.decode('cp936').encode('utf-8'),weather2.decode('cp936').encode('utf-8'))

account_sid = "AC58f035f3406ae3563b4507531724cb0c"
auth_token = "0fcddc31c0cff4db69be9d0be33b7ae2"

client = Client(account_sid,auth_token)


message = client.messages.create(
    to = "+8618611207658",
    from_ = "+13345818054",
    body= weather)
print (message.sid)