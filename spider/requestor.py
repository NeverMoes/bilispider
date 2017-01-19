import requests
from .consts import const
from .parser import *
import http.cookiejar as cookielib
import logging
import sys


class Requestor(object):
    def __init__(self):
        self.requestors = [self.request_stat, self.request_html]
        self.init_session()
        self.init_logger()

    def init_session(self):
        self.session = requests.session()
        self.session.cookies = cookielib.LWPCookieJar(filename=const.COOKIES_PATH)
        self.session.cookies.load(ignore_discard=True)

    def init_logger(self):
        # log conf
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(const.ERRLOG_PATH)
        file_handler.setLevel(logging.WARNING)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def start_request(self, avnum):
        parsers = list()
        self.logger.info('requesting av {avnum}'.format(avnum=avnum))
        for requestor in self.requestors:
            parser = requestor(avnum)
            parsers.append(parser)
        return parsers

    def request_stat(self, avnum, retry=5):
        url = const.API_STAT_FORMAT.format(avnum=avnum)

        while retry:
            try:
                req = self.session.get(url, timeout=10)
            except Exception:
                retry -= 1
                continue
            else:
                return ParserStat(raw_data=req.text)

        raise Exception('request_stat failed'.format(avnum=avnum))

    def request_html(self, avnum, retry=5):
        url = const.HTML_PAGE_FORMAT.format(avnum=avnum)

        while retry:
            try:
                req = self.session.get(url, timeout=10)
            except Exception:
                retry -= 1
                continue
            else:
                return ParserHtml(raw_data=req.text)

        raise Exception('request_html failed'.format(avnum=avnum))
