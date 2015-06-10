from app001.utils.settings import DB_SETTINGS
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
        self.logger = get_logger(__file__)
        self.on_heroku = bool(os.environ.get('ON_HEROKU', None))

        if not self.on_heroku:
            self.connection = connect(DB_SETTINGS['LOCAL']['DB_NAME'],
                                      host=DB_SETTINGS['LOCAL']['DB_HOST'],
                                      port=DB_SETTINGS['LOCAL']['DB_PORT'])
        else:
            self.connection = connect(DB_SETTINGS['REMOTE']['DB_NAME'],
                                      host=DB_SETTINGS['REMOTE']['DB_HOST'],
                                      port=DB_SETTINGS['REMOTE']['DB_PORT'],
                                      username=DB_SETTINGS[
                                          'REMOTE']['DB_USER'],
                                      password=DB_SETTINGS['REMOTE']['DB_PASS'])

    def __enter__(self):
        """Starts a new Connection by returning the mongoengine connection object

        """
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exits the Connection by closing the mongoengine connection object

        """
        if exc_type:
            self.logger.debug(
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
