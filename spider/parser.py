import re
import json


class Parser(object):
    def __init__(self, raw_data=None):
        self.raw_data = raw_data

    def parse(self, item):
        raise Exception('unimplement error')


class ParserStat(Parser):
    re_pat = re.compile(r'\((.+)\)')

    def __init__(self, raw_data):
        super().__init__(raw_data)

    def parse(self, item):
        if not item:
            pass
        jsonstr = self.re_pat.findall(self.raw_data)[0]
        jsondic = json.loads(jsonstr)['data']
        item.info['view'] = jsondic['view']
        item.info['danmaku'] = jsondic['danmaku']
        item.info['reply'] = jsondic['reply']
        item.info['fav'] = jsondic['favorite']
        item.info['share'] = jsondic['share']


