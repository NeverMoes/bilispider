import logging
from .requestor import Requestor
from .item import VideoInfo
from .infosaver import InfoSaver
from .consts import const
import sys
from multiprocessing.dummy import Pool as ThreadPool
import time

class Engine(object):
    def __init__(self):
        self.requestor = Requestor()
        self.infosaver = InfoSaver()
        self.pool = ThreadPool(6)

    def start(self, avnum):
        start = time.time()
        self.pool.map(self.task, range(avnum, 100))
        print(time.time()-start)

    def task(self, avnum):
        videoinfo = VideoInfo(avnum)
        try:
            parsers = self.requestor.start_request(avnum)
        except Exception:
            self.logger.exception('cant request {avnum}'.format(avnum=avnum))
        else:
            videoinfo.build(parsers)
            self.infosaver.add_data(videoinfo.data)
        finally:
            return

    def init_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(const.ERRLOG_PATH)
        file_handler.setLevel(logging.WARNING)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

