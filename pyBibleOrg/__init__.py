__author__ = 'khatcher'

import requests


def getVOTD():
    r = requests.get('http://labs.bible.org/api/?passage=votd&type=text&formatting=full')
    return r.content



#VOTD  http://labs.bible.org/api/?passage=votd&type=text&formatting=full