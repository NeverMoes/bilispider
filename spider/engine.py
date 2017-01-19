import logging
from .requestor import Requestor
from .infobuilder import InfoBuilder
from .infosaver import InfoSaver
from .consts import const
import sys


def main(avnum):
    logger = init_logger()

    requestor = Requestor()
    infobuilder = InfoBuilder()
    infosaver = InfoSaver()

    while True:
        try:
            parsers = requestor.start_request(avnum)
        except Exception:
            logger.exception('cant request {avnum}'.format(avnum=avnum))
        else:
            infobuilder.start_build(avnum, parsers)
            data = infobuilder.get_data()
            infosaver.add_data(data)
        finally:
            avnum+=1


def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(const.ERRLOG_PATH)
    file_handler.setLevel(logging.WARNING)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


