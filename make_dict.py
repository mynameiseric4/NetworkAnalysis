from bs4 import BeautifulSoup
import numpy as np

with open('/Users/ericyatskowitz/Downloads/enwiki-20170420-pages-articles.xml', 'r') as xml_doc:
    soup = BeautifulSoup(xml_doc, 'xml')
tags = soup.find_all('title')
hl_tags = soup.find_all('text')
net_dict = {}
for i in xrange(len(tags)-1):
    new_tags = []
    word = ''
    flag = False
    for letter in hl_tags[i].text:
        if flag == True:
            if word == u'[[' and letter == u'[':
                continue
            word += letter
            if letter == u'[':
                flag = False
                word = ''
                continue
            if word[-2:] == u']]':
                new_tags.append(word.strip('\[\]').lower().split('|')[0])
                flag = False
                word = ''
            continue
        if letter == u'[':
            word += letter
        if word == u'[' and letter != u'[':
            word = ''
        if word == u'[' and letter == u'[':
            word += letter
            flag = True
    net_dict[tags[i].text.lower()] = new_tags

np.save('net_dict.npy', net_dict)
