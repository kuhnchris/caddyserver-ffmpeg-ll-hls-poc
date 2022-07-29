import typing
import logging
import uwsgi

logger = logging.getLogger(__name__)
logger.debug('Test module loaded')


def dispatch(env: dict, start_response: typing.Callable) -> typing.Generator[bytes, None, None]:

    if env.get('HTTP_TRANSFER_ENCODING', '').lower() == 'chunked':
        while _ := uwsgi.chunked_read(30):
            pass

    start_response(
        '200 OK',
        [
            ('Content-Type', 'text/plain'),
            ('Content-Length', '2')
        ]
    )

    yield b'OK'
