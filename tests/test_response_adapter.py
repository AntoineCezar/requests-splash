import unittest
import json
import io

import requests

from requests_splash.response_adapter import ResponseAdapter
from requests_splash.response_adapter import map_splash_response


class TestAdaptResponse(unittest.TestCase):

    def setUp(self):
        self.adapter = ResponseAdapter()

    def history_response(self, url, status=302, status_text='Found',
                         headers={}):
        return {
            'response': {
                'url': url,
                'status': status,
                'statusText': status_text,
                'headers': [
                    {'name': name, 'value': value}
                    for name, value in headers.items()
                ],
            },
        }

    def splash_response(self, html='', history=[]):
        response = requests.Response()

        if not history:
            history = [
                self.history_response('http://exemple.url', 200, 'OK'),
            ]

        response.raw = io.BytesIO(json.dumps({
            'history': history,
            'html': html,
        }).encode())

        return response

    def test_reponse_url_is_the_last_history_response_url(self):
        expected_url = 'http://expected.url'

        response = self.adapter.adapt_response(self.splash_response(history=[
            self.history_response(expected_url),
            self.history_response('http://wrong.url'),
        ]))

        self.assertEqual(response.url, expected_url)

    def test_reponse_status_code_is_the_last_history_response_status(self):
        status = 200

        response = self.adapter.adapt_response(self.splash_response(history=[
            self.history_response('http://second.url', status=status),
            self.history_response('http://first.url'),
        ]))

        self.assertEqual(response.status_code, status)

    def test_reponse_reason_is_the_last_history_response_status_text(self):
        reason = 'Some Reason'

        response = self.adapter.adapt_response(self.splash_response(history=[
            self.history_response('http://second.url', status_text=reason),
            self.history_response('http://first.url'),
        ]))

        self.assertEqual(response.reason, reason)

    def test_reponse_headers_are_the_last_history_response_headers(self):
        headers = {
            'header1': 'value1',
            'header2': 'value2',
        }

        response = self.adapter.adapt_response(self.splash_response(history=[
            self.history_response('http://second.url', headers=headers),
            self.history_response('http://first.url'),
        ]))

        self.assertEqual(response.headers, headers)

    def test_reponse_history_has_oldest_response_first(self):
        history = [
            self.history_response('http://last.url'),
            self.history_response('http://second.url'),
            self.history_response('http://first.url')
        ]

        response = self.adapter.adapt_response(
            self.splash_response(history=history)
        )

        self.assertEqual([
            response.url
            for response in response.history
        ], [
            map_splash_response(item['response']).url
            for item in reversed(history[1:])
        ])

    def test_reponse_content_is_the_encoded_splash_html_result(self):
        html = 'some content'

        response = self.adapter.adapt_response(self.splash_response(html=html))

        self.assertEqual(response.content, html.encode())
