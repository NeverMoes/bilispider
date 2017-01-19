import re
import json
from lxml import etree


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
        jsonstr = self.re_pat.findall(self.raw_data)[0]
        jsondic = json.loads(jsonstr)['data']
        item.info['view'] = jsondic['view']
        print(item.info['view'])
        item.info['danmaku'] = jsondic['danmaku']
        item.info['reply'] = jsondic['reply']
        item.info['fav'] = jsondic['favorite']
        item.info['share'] = jsondic['share']

class ParserHtml(Parser):
    def __init__(self, raw_data):
        super().__init__(raw_data)

    def parse(self, item):
        parsed = etree.HTML(self.raw_data)
        item.info['title'] = parsed.xpath('//title')[0].text.split('_')[0]
        keywords = parsed.xpath('//meta[@name="keywords"]/@content')[0].split(',')
        try:
            item.info['author'] = keywords[6]
            item.info['category1'] = keywords[4]
            item.info['category2'] = keywords[5]
            item.info['tags'] = ','.join(keywords[7::])
        except Exception:
            item.info['author'] = 'None'
            item.info['category1'] = 'None'
            item.info['category2'] = 'None'
            item.info['tags'] = 'None'


