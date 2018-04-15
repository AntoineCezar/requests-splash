from requests import Session
from requests.adapters import BaseAdapter

from .request_adapter import RequestAdapter
from .response_adapter import ResponseAdapter


class SplashAdapter(BaseAdapter):

    def __init__(self, splash_url,
                 request_adapter_factory=RequestAdapter,
                 response_adapter_factory=ResponseAdapter,
                 session_factory=Session):
        self._request_adapter = request_adapter_factory(splash_url)
        self._response_adapter = response_adapter_factory()
        self._session = session_factory()

    def send(self, request, stream=False, timeout=None, verify=True,
             cert=None, proxies=None):
        splash_request = self._request_adapter.adapt_request(request)
        splash_response = self._session.send(splash_request)
        response = self._response_adapter.adapt_response(splash_response)
        return response

    def close(self):
        self._session.close()
