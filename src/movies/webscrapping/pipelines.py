import logging

from pymongo import MongoClient
from scrapy.exceptions import DropItem

from .settings import MONGODB_SERVER, MONGODB_PORT, MONGODB_DB, MONGODB_COLLECTION


class MongoDBPipeline(object):

    def __init__(self):

        cnxn = MongoClient(
            MONGODB_SERVER,
            MONGODB_PORT,
        )
        db = cnxn[MONGODB_DB]
        self.collection = db[MONGODB_COLLECTION]

    def process_item(self, item, spider):

        valid = True
        logger = logging.getLogger()

        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        if valid:
            self.collection.insert(dict(item))
            logger.info("Movie data added to MongoDB database.")

        return item
