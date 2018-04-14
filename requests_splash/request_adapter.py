import urllib.parse

from requests import PreparedRequest
from requests import Request


class RequestAdapter:

    def __init__(self, splash_url):
        self._url = urllib.parse.urljoin(splash_url, '/render.json')

    def adapt_request(self, request: PreparedRequest) -> PreparedRequest:
        data = {
            'url': request.url,
            'html': 1,
            'history': 1,
        }

        splash_request = Request('POST', self._url, json=data)

        return splash_request.prepare()
