class VideoInfo(object):
    def __init__(self, avnum):
        self.av = avnum
        self.info = dict()

    def __str__(self):
        return str(self.av)+str(self.info)


class InfoBuilder(object):
    def start_build(self, avnum, parsers):
        self.info = VideoInfo(avnum)

        for parser in parsers:
            parser.parse(self.info)

    def get_info(self):
        return self.info

