import secrets
import string

from app.models import URL


def generate_slug(min_length: int = 6, max_length: int = 10) -> str:
    charset = string.ascii_lowercase + string.digits

    while True:
        length = secrets.choice(range(min_length, max_length + 1))
        slug = ''.join(secrets.choice(charset) for _ in range(length))

        if not URL.objects.filter(slug=slug).exists():
            return slug
