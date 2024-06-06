import secrets
import string

from app.models import URL


def generate_short_url(min_length: int = 6, max_length: int = 10) -> str:
    charset = string.ascii_lowercase + string.digits

    while True:
        length = min_length + secrets.randint(0, max_length - min_length)
        short_url = ''.join(secrets.choice(charset) for _ in range(length))

        if not URL.objects.filter(short_url=short_url).exists():
            return short_url
