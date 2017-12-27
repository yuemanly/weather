# -*- coding: cp936 -*-
import urllib2
import json
from city import city

cityname = raw_input('what is the city of weather do you want to know?\n')
print cityname
cityname = cityname.encode('cp936')
print cityname
citycode = city.get(cityname)
if citycode:
    try:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)

        content = urllib2.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_temp = ('%s\n%s ~ %s') % (
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print str_temp
    except:
        print 'Wrong!'
else:
    print 'Cant find the city.'
