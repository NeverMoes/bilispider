from .requestor import Requestor
from .infobuilder import InfoBuilder
from .infosaver import InfoSaver


def main():

    avnum = 6536710
    # avnum = 1
    requestor = Requestor()
    infobuilder = InfoBuilder()
    infosaver = InfoSaver()
    parsers = requestor.start_request(avnum)
    infobuilder.start_build(avnum, parsers)
    print(infobuilder.get_data())
    infosaver.add_data(infobuilder.get_data())


