# 452-Final
This is 452 final project that is to get pictures in the website using Spider.

#Code here
import re
import requests
import os
class Spider:
    def savePageInfo(self, _url, _position, _regX):
        url = _url
        position = _position
        html = requests.get(url).text
        regX = _regX
        pic_url = re.findall(regX,html,re.S)
        i = 0
        for each in pic_url:
            pic = requests.get( each )
            print(url+each)

            # if the folder doesn't exist, then build one
            if not os.path.isdir(position):
                os.makedirs(position)

            fp = open( position+str(i)+'.jpg', 'wb' )
            fp.write(pic.content)
            # print position+each
            fp.close()
            i+=1

position_end = ''
url = 'https://www.zara.com/' + position_end   # The url of target website
position = '/Users/fanyushuo//Documents/spider pictures/' + position_end   # Position of the folder that saves pictures
regX = 'name _item" href=(.*?) t'
spider = Spider()
spider.savePageInfo(url, position, regX)
