from config.settings import PROTOCOL, DEFAULT_HOST, DEFAULT_PORT

SHORT_URL_LENGTH = 10
TRIALS_NO = 3


def get_server():
    return f'{PROTOCOL}://{DEFAULT_HOST}:{DEFAULT_PORT}/'
