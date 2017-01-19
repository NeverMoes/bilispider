import os


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError('Cant change const %s.' % name)
        if not name.isupper():
            raise self.ConstCaseError(
                'const name %s is not all uppercase' % name)
        self.__dict__[name] = value


const = _const()


##################################################################################################


const.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
const.COOKIES_PATH = os.path.join(const.BASE_DIR, 'spider', 'bilicookies')
const.ERRLOG_PATH = os.path.join(const.BASE_DIR, 'spider', 'errlog')

##################################################################################################


const.HTML_PAGE_FORMAT = 'http://www.bilibili.com/video/av{avnum}/'


##################################################################################################

# 一些基本的视频信息

const.API_STAT_FORMAT = 'http://api.bilibili.com/archive_stat/stat?callback=jQuery17206695986036376824_1483704956932&aid={avnum}&type=jsonp&_=1483704957610'


'''
http://api.bilibili.com/archive_stat/stat?callback=jQuery17206695986036376824_1483704956932&aid=6536710&type=jsonp&_=1483704957610

jQuery17206695986036376824_1483704956932({"code":0,"data":{"view":"--","danmaku":1177,"reply":297,"favorite":24511,"coin":1696,"share":385,"now_rank":0,"his_rank":85},"message":""});
'''

##################################################################################################

#视频的tag信息

'http://api.bilibili.com/x/tag/archive/tags?callback=jQuery17202870352235622704_1482889079894&aid=170001&jsonp=jsonp&_=1482889080659'

##################################################################################################


