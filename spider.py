import requests
import re
import json
from consts import const

req = requests.get(const.API_STAT_FORMAT.format(av=6536710))
response = req.content.decode('utf')


def parser(content):
    pat_api_stat = re.compile(r'\((.+)\)')
    jsonstr = pat_api_stat.findall(content)[0]
    jsondic = json.loads(jsonstr)
    return jsondic


data = parser(response)

print(data)

print(req.content)


# class VideoInfo(object):
#     def __init__(self, av):
#         self.av = av
#
#
#
#     @staticmethod
#     def test_api():
#         pass