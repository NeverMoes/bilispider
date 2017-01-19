import sqlalchemy as sam
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .local import dbconf
import logging
from .consts import const
import sys


engine = sam.create_engine(
    "mysql+pymysql://{username}:{password}@{hostname}/{dbname}?charset=utf8".format(username=dbconf['username'],
                                                                                    password=dbconf['password'],
                                                                                    hostname=dbconf['hostname'],
                                                                                    dbname=dbconf['dbname']),
    encoding="utf8", echo=False)

BaseModel = declarative_base()


class Video(BaseModel):
    __tablename__ = 'videoinfo'
    __table_args__ = {
        "mysql_engine": "InnoDB",
        "mysql_charset": "utf8",
    }

    av = sam.Column('av', sam.Integer, primary_key=True)

    view = sam.Column('view', sam.Integer, nullable=True)
    fav = sam.Column('fav', sam.Integer, nullable=False)
    danmaku = sam.Column('danmaku', sam.Integer, nullable=False)
    reply = sam.Column('reply', sam.Integer, nullable=False)
    share = sam.Column('share', sam.Integer, nullable=False)

    title = sam.Column('title', sam.String(100), nullable=False)
    author = sam.Column('author', sam.String(50), nullable=False)
    category1 = sam.Column('category1', sam.String(20), nullable=False)
    category2 = sam.Column('category2', sam.String(20), nullable=False)
    tags = sam.Column('tags', sam.String(200), nullable=False)


class InfoSaver(object):
    def __init__(self):
        BaseModel.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()
        self.init_logger()

    def init_logger(self):
        # log conf
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(const.ERRLOG_PATH)
        file_handler.setLevel(logging.WARNING)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def add_data(self, data):
        self.session.add(Video(**data))
        self.logger.info(str(data))
        self.session.commit()


