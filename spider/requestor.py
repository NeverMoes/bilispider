import requests
from .consts import const
from .parser import *
import http.cookiejar as cookielib


class Requestor(object):
    def __init__(self):
        self.requestors = [self.request_stat, self.request_html]
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename=const.COOKIES_PATH)
        self.session.cookies.load(ignore_discard=True)

    def start_request(self, avnum):
        parsers = list()
        for requestor in self.requestors:
            parser = requestor(avnum)
            parsers.append(parser)
        return parsers

    def request_stat(self, avnum):
        url = const.API_STAT_FORMAT.format(avnum=avnum)
        req = self.session.get(url)
        return ParserStat(raw_data=req.text)

    def request_html(self, avnum):
        url = const.HTML_PAGE_FORMAT.format(avnum=avnum)
        req = self.session.get(url)
        return ParserHtml(raw_data=req.text)
