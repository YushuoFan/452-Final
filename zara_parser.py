from html.parser import HTMLParser
import os
from subprocess import call

jackets_list = []

# create a subclass and override the handler methods
class ZaraParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
    	if tag=='img':
            if type(attrs) == list and len(attrs) == 4 :
                name = attrs[2][1]
                path = "https:"+attrs[3][1]
                if '.jpg' in path:
                    jackets_list.append((name, path))

# instantiate the parser and fed it some HTML
parser = ZaraParser()

file = open('./jackets.html', 'r')
parser.feed(file.read())

print(len(jackets_list))
print(jackets_list)


i = 1
for jacket in jackets_list :
    filepath = './images/' + str(i) + '_' + jacket[0].replace(' ', '_') + '.jpg'
    os.system('wget '+jacket[1] + ' -O '+ filepath)
    i = i + 1
