import unittest
import json

import requests

from requests_splash.request_adapter import RequestAdapter


class TestAdaptRequest(unittest.TestCase):

    def setUp(self):
        self.splash_url = 'http://localhost:8085'
        self.splash_json_render_url = self.splash_url + '/render.json'
        self.adapter = RequestAdapter(self.splash_url)

    def prepared_get(self, url='http://example.com', **kwargs):
        return requests.Request('GET', url, **kwargs).prepare()

    def test_splash_request_url_is_splash_json_render_url(self):
        request = self.prepared_get()

        splash_request = self.adapter.adapt_request(request)

        self.assertEqual(splash_request.url, self.splash_json_render_url)

    def test_splash_request_method_is_post(self):
        request = self.prepared_get()

        splash_request = self.adapter.adapt_request(request)

        self.assertEqual(splash_request.method, 'POST')

    def test_splash_request_url_option_is_request_url(self):
        request = self.prepared_get()

        splash_request = self.adapter.adapt_request(request)

        self.assertEqual(json.loads(splash_request.body)['url'], request.url)

    def test_splash_request_has_html_option_on(self):
        request = self.prepared_get()

        splash_request = self.adapter.adapt_request(request)

        self.assertEqual(json.loads(splash_request.body)['html'], 1)

    def test_splash_request_has_history_option_on(self):
        request = self.prepared_get()

        splash_request = self.adapter.adapt_request(request)

        self.assertEqual(json.loads(splash_request.body)['history'], 1)
