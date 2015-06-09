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

    def test_add_reviews(self):
        """Test add reviews functionality

        """
        biz1 = {'name': 'kohls', 'location': '30.9538, 24.4383'}
        review1 = {'name': 'kohls', 'rating': 5,
                   'review': 'good', 'tags': 'shopping, jersey'}

        with self.test_request_context():
            resp1 = self.test_client().post('/business/add',
                                            data=json.dumps(biz1),
                                            content_type='application/json'
                                            )
            resp2 = self.test_client().post('/business/review',
                                            data=json.dumps(review1),
                                            content_type='application/json'
                                            )

        self.assertEqual(resp2.status_code, 200)

    def test_get_business_info(self):
        """Test get business info functionality

        """
        biz1 = {'name': 'markers', 'location': '34.2738, 20.9320'}
        biz2 = {'name': 'kohls', 'location': '30.9538, 24.4383'}
        biz3 = {'name': 'pepboys', 'location': '30.2232, -20.2221'}
        biz4 = {'name': 'massage envy', 'location': '40.3895, -10.4229'}
        review1 = {'name': 'kohls', 'rating': 5,
                   'review': 'good', 'tags': 'shopping, jersey'}
        review2 = {'name': 'markers', 'rating': 5,
                   'review': 'excellent', 'tags': 'bars, restaurants'}
        review3 = {'name': 'pepboys', 'rating': 3,
                   'review': 'okay', 'tags': 'automobile, repairs'}
        review4 = {'name': 'pepboys', 'rating': 2,
                   'review': 'bad', 'tags': 'tires, automobile'}
        review5 = {'name': 'kohls', 'rating': 1,
                   'review': 'worst', 'tags': 'clothing, jersey'}
        review6 = {'name': 'markers', 'rating': 3,
                   'review': 'alright', 'tags': 'beer, sandwich'}
        review7 = {'name': 'pepboys', 'rating': 5,
                   'review': 'great', 'tags': 'engine, oil'}
        review8 = {'name': 'kohls', 'rating': 3,
                   'review': 'okay', 'tags': 'shopping, nyc'}
        review9 = {'name': 'markers', 'rating': 1,
                   'review': 'bad', 'tags': 'eatery, classy'}

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
            resp4 = self.test_client().post('/business/add',
                                            data=json.dumps(biz4),
                                            content_type='application/json'
                                            )
            resp5 = self.test_client().post('/business/review',
                                            data=json.dumps(review1),
                                            content_type='application/json'
                                            )
            resp6 = self.test_client().post('/business/review',
                                            data=json.dumps(review2),
                                            content_type='application/json'
                                            )
            resp7 = self.test_client().post('/business/review',
                                            data=json.dumps(review3),
                                            content_type='application/json'
                                            )
            resp8 = self.test_client().post('/business/review',
                                            data=json.dumps(review4),
                                            content_type='application/json'
                                            )
            resp9 = self.test_client().post('/business/review',
                                            data=json.dumps(review5),
                                            content_type='application/json'
                                            )
            resp10 = self.test_client().post('/business/review',
                                             data=json.dumps(review6),
                                             content_type='application/json'
                                             )
            resp11 = self.test_client().post('/business/review',
                                             data=json.dumps(review7),
                                             content_type='application/json'
                                             )
            resp12 = self.test_client().post('/business/review',
                                             data=json.dumps(review8),
                                             content_type='application/json'
                                             )
            resp13 = self.test_client().post('/business/review',
                                             data=json.dumps(review9),
                                             content_type='application/json'
                                             )

            resp14 = self.test_client().get('/business/info/kohls')
            resp15 = self.test_client().get('/business/info/pepboys')
            resp16 = self.test_client().get('/business/info/markers')

        json_response_1 = json.loads(resp14.data.decode())
        json_response_2 = json.loads(resp15.data.decode())
        json_response_3 = json.loads(resp16.data.decode())

        self.assertEqual(resp14.status_code, 200)
        self.assertEqual(resp15.status_code, 200)
        self.assertEqual(resp16.status_code, 200)

        self.assertEqual(len(json_response_1['business_info']['reviews']), 3)
        self.assertEqual(len(json_response_2['business_info']['reviews']), 3)
        self.assertEqual(len(json_response_3['business_info']['reviews']), 3)

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
