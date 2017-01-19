class VideoInfo(object):
    def __init__(self, avnum):
        self.av = avnum
        self.info = dict()

    def __str__(self):
        return str(self.av) + ': ' + str(self.info)

    def build(self, parsers):
        for parser in parsers:
            parser.parse(self)

    @property
    def data(self):
        if self.info['view'] == '--':
            self.info['view'] = None
        self.info.update(av=self.av)
        return self.info




