import requests
from .consts import const
from .parser import *


class Requestor(object):
    def __init__(self):
        self.requestors = [self.request_stat, ]

    def start_request(self, avnum):
        parsers = list()
        for requestor in self.requestors:
            parser = requestor(avnum)
            parsers.append(parser)
        return parsers

    def request_stat(self, avnum):
        api_url = const.API_STAT_FORMAT.format(avnum=avnum)
        req = requests.get(api_url)
        return ParserStat(raw_data=req.text)



