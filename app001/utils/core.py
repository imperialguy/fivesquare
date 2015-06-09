from mongoengine import connect
import logging
import sys


class Connection(object):

    """For providing a connection interface accross RESTful requests.

    """

    def __init__(self, **kwargs):
        """Constructor to setup the connection object

        """
        self.connection = connect(kwargs.get('db_name', 'fivesquare'),
                                  host=kwargs.get('db_host', 'localhost'),
                                  port=kwargs.get('db_port', 27017))

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
