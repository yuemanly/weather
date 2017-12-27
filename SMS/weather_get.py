#-------------------------------------------------------------------------------
# -*- coding: UTF-8 -*-
# Name:        weather_get
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

import urllib2
import json


name = "朝阳"
citycode = '101010300'

if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)

        content = urllib2.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s\n%s ~ %s') % (
            name.decode('utf-8').encode('cp936'),
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print str_temp
        f = open('D:\git\pythonlearning\weather\SMS\data.txt','w')
        f.write(str_temp)
        f.close()
    except:
        print 'Wrong!'
else:
    print 'Cant find the city.'

