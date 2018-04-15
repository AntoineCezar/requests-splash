import requests

from .splash_adapter import SplashAdapter


DEFAULT_SPLASH_URL = 'http://localhost:8050'


class Session(requests.Session):

    def __init__(self, *args,
                 splash_url=DEFAULT_SPLASH_URL,
                 splash_adapter_factory=SplashAdapter,
                 **kwargs):
        super().__init__(*args, **kwargs)
        splash_adapter = splash_adapter_factory(splash_url)
        self.mount('http://', splash_adapter)
        self.mount('https://', splash_adapter)
