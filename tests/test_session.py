import unittest
import unittest.mock

from requests_splash.session import DEFAULT_SPLASH_URL
from requests_splash.session import Session


class TestInit(unittest.TestCase):

    def test_it_creates_request_adapter_with_provided_splash_url(self):
        splash_url = unittest.mock.sentinel.splash_url
        splash_adapter_factory = unittest.mock.Mock()

        Session(
            splash_url=splash_url,
            splash_adapter_factory=splash_adapter_factory,
        )

        splash_adapter_factory.assert_called_once_with(splash_url)

    def test_it_creates_request_adapter_with_default_splash_url(self):
        splash_adapter_factory = unittest.mock.Mock()

        Session(
            splash_adapter_factory=splash_adapter_factory,
        )

        splash_adapter_factory.assert_called_once_with(DEFAULT_SPLASH_URL)
