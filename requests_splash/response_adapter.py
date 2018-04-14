import io

from requests import Response


def map_splash_response(data: dict) -> Response:
    response = Response()
    response.url = data['url']
    response.status_code = data['status']
    response.reason = data['statusText']
    response.headers = {
        header['name']: header['value']
        for header in data['headers']
    }

    return response


class ResponseAdapter:

    def adapt_response(self, splash_response: Response) -> Response:
        data = splash_response.json()

        response = map_splash_response(data['history'][0]['response'])
        response.history = [
            map_splash_response(item['response'])
            for item in reversed(data['history'][1:])
        ]
        response.raw = io.BytesIO(data['html'].encode())

        return response
