import os
import unittest

from flaskerino import app
from flaskerino.views import fetch_images

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_main_page_index(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        response = self.app.get('/fail', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    # test fetch_images() count
    def test_image_count(self):
        self.assertEqual(len(fetch_images()), 4)

    # test fetch_images() objects
    def test_images_detail(self):
        rv = fetch_images()
        for item in rv:
            assert item['width'] < 500
            assert b'.jpg' in item['image_path']
            assert b'.jpg' in item['thumb_path']
            assert "" != item['name']


if __name__ == "__main__":
    unittest.main()

