import os
import unittest
import sys

# Append the above path to allow us to relative import the below
sys.path.append('.')

from flaskerino import app
from flaskerino import fetch_images

class BasicTests(unittest.TestCase):
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

    # test fetch_images() width
    def test_images_width(self):
        rv = fetch_images()
        for item in rv:
            assert item['width'] < 500

if __name__ == "__main__":
    unittest.main()
