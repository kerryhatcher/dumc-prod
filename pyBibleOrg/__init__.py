__author__ = 'khatcher'

import requests


def getVOTD():
    votd = ''
    try:
        r = requests.get('http://labs.bible.org/api/?passage=votd&type=text&formatting=full')
        votd = r.content
    except:
        votd = 'no nonnection'
    return votd



#VOTD  http://labs.bible.org/api/?passage=votd&type=text&formatting=full