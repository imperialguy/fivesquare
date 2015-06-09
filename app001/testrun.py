from flask import json, url_for
import unittest2 as unittest
import os
import sys
import json


class TestApp001(unittest.TestCase):

    """Simple test for app001

    """

    def setUp(self):
        """Setup the db tables

        """
        setupdb.refresh()
        self.test_client = app.test_client
        self.test_request_context = app.test_request_context

    def test_add_business(self):
        """Test add business functionality

        """
        biz1 = {'name': 'markers', 'location': '34.2738, 20.9320'}
        biz2 = {'name': 'kohls', 'location': '30.9538, 24.4383'}
        biz3 = {'name': 'mcdonalds', 'location': '30.2232, -20.2221'}

        with self.test_request_context():
            resp1 = self.test_client().post('/business/add',
                                            data=json.dumps(biz1),
                                            content_type='application/json'
                                            )
            resp2 = self.test_client().post('/business/add',
                                            data=json.dumps(biz2),
                                            content_type='application/json'
                                            )
            resp3 = self.test_client().post('/business/add',
                                            data=json.dumps(biz3),
                                            content_type='application/json'
                                            )

        self.assertEqual(resp1.status_code, 200)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(resp3.status_code, 200)

    def test_search_businesses(self):
        """Test search businesses functionality

        """
        biz1 = {'name': 'markers', 'location': '34.2738, 20.9320'}
        biz2 = {'name': 'kohls', 'location': '30.9538, 24.4383'}
        biz3 = {'name': 'mcdonalds', 'location': '30.2232, -20.2221'}
        param1 = {'location': '29.4833, 22.18930', 'radius': 5}

        with self.test_request_context():
            resp1 = self.test_client().post('/business/add',
                                            data=json.dumps(biz1),
                                            content_type='application/json'
                                            )
            resp2 = self.test_client().post('/business/add',
                                            data=json.dumps(biz2),
                                            content_type='application/json'
                                            )
            resp3 = self.test_client().post('/business/add',
                                            data=json.dumps(biz3),
                                            content_type='application/json'
                                            )
            resp4 = self.test_client().post('/business/search',
                                            data=json.dumps(param1),
                                            content_type='application/json'
                                            )

        json_response = json.loads(resp4.data.decode())

        self.assertEqual(resp4.status_code, 200, resp4.data)
        self.assertEqual(len(json_response[u'businessses']), 2)

    def tearDown(self):
        """Clear the db

        """
        setupdb.refresh()


def main():
    unittest.main()


if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, BASE_DIR)
    from app001.utils import setupdb
    from app001.web.app import app
    from app001.web.views import business
    main()
