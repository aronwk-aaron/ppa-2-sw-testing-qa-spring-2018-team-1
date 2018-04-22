import pytest
import time
from urllib import request, parse, error

from flask import url_for, abort
from selenium import webdriver
from flask_testing import LiveServerTestCase

from app import create_app


class TestBase(LiveServerTestCase):
    def create_app(self):
        config_name = 'dev'
        app = create_app(config_name)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.get(self.get_server_url())

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)


class TestViews(TestBase):

    def test_index_view(self):
        response = self.client.get(url_for('main.index'))
        assert response.status_code == 200
