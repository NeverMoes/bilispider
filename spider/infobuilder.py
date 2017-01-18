class VideoInfo(object):
    def __init__(self, avnum):
        self.av = avnum
        self.info = dict()

    def __str__(self):
        return str(self.av) + ': ' + str(self.info)

    @property
    def data(self):
        if self.info['view'] == '--':
            self.info['view'] = None
        self.info.update(av=self.av)
        return self.info


class InfoBuilder(object):
    def start_build(self, avnum, parsers):
        self.videoinfo = VideoInfo(avnum)

        for parser in parsers:
            parser.parse(self.videoinfo)

    def get_data(self):
        return self.videoinfo.data

