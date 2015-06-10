from app001.utils.settings import DB_NAME, DB_HOST, DB_PORT
from mongoengine import connect
import logging
import sys
import os


class Connection(object):

    """For providing a connection interface accross RESTful requests.

    """

    def __init__(self):
        """Constructor to setup the connection object

        """
        MONGO_URI = os.environ.get('MONGOHQ_URL', None)
        db_name = 'fivesquare' if not MONGO_URI else MONGO_URI.split("/")[-1]
        db_host = MONGO_URI if MONGO_URI else 'localhost'
        db_port = DB_PORT
        self.connection = connect(db_name, host=db_host, port=db_port)

    def __enter__(self):
        """Starts a new Connection by returning the mongoengine connection object

        """
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exits the Connection by closing the mongoengine connection object

        """
        if exc_type:
            logger = get_logger(__name__)
            logger.debug(
                'the following exception occured:\n{0}'.format(exc_val))
        self.connection.disconnect()
        return True


def get_logger(filename):
    logger = logging.getLogger(filename)
    logger.setLevel(logging.DEBUG)
    channel = logging.StreamHandler(sys.stdout)
    channel.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    channel.setFormatter(formatter)
    logger.addHandler(channel)

    return logger
