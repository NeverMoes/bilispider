from .requestor import Requestor
from .infobuilder import InfoBuilder


def main():

    avnum = 6536710

    requestor = Requestor()
    infobuilder = InfoBuilder()
    parsers = requestor.start_request(avnum)
    infobuilder.start_build(avnum, parsers)

    print(infobuilder.get_info())


