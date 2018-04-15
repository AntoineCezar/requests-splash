import unittest
import unittest.mock

import requests

from requests_splash.request_adapter import RequestAdapter
from requests_splash.response_adapter import ResponseAdapter
from requests_splash.splash_adapter import SplashAdapter


class SplashAdapterTestCase(unittest.TestCase):

    def setUp(self):
        self.session = unittest.mock.Mock(requests.Session)
        self.splash_url = unittest.mock.sentinel.splash_url
        self.request_adapter = unittest.mock.Mock(RequestAdapter)
        self.response_adapter = unittest.mock.Mock(ResponseAdapter)
        self.adapter = SplashAdapter(
            splash_url=self.splash_url,
            request_adapter_factory=lambda _: self.request_adapter,
            response_adapter_factory=lambda: self.response_adapter,
            session_factory=lambda: self.session,
        )


class TestInit(SplashAdapterTestCase):

    def test_it_creates_request_adapter_with_provided_splash_url(self):
        request_adapter_factory = unittest.mock.Mock()

        SplashAdapter(
            splash_url=self.splash_url,
            request_adapter_factory=request_adapter_factory,
            response_adapter_factory=lambda: self.response_adapter,
            session_factory=lambda: self.session,
        )

        request_adapter_factory.assert_called_once_with(self.splash_url)


class TestSend(SplashAdapterTestCase):

    def prepared_get(self, url='http://example.com', **kwargs):
        return requests.Request('GET', url, **kwargs).prepare()

    def test_it_adapts_request(self):
        request = self.prepared_get()
        adapted_request = unittest.mock.sentinel.request
        self.request_adapter.adapt_request.return_value = adapted_request

        self.adapter.send(request)

        self.session.send.assert_called_once_with(adapted_request)

    def test_it_adapts_response(self):
        request = self.prepared_get()
        adapted_response = unittest.mock.sentinel.adapted_response
        self.response_adapter.adapt_response.return_value = adapted_response

        response = self.adapter.send(request)

        self.assertEqual(response, adapted_response)


class TestClose(SplashAdapterTestCase):

    def test_it_closes_session(self):
        self.adapter.close()

        self.session.close.assert_called_once()
