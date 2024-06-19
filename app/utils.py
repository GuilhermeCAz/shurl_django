import secrets
import string

from app.models import URL


def generate_slug(min_length: int = 6, max_length: int = 10) -> str:
    """
    Generate a slug.

    Keyword Arguments:
        min_length (int, optional): The minimum length of the slug.
        (default: {6})
        max_length (int, optional): The maximum length of the slug.
        (default: {10})

    Returns:
        str: The generated slug. A slug is a string composed of ASCII letters
        and numbers, hyphens and underscores, and it must be at least 6
        and no more than 10 characters in length. The slug must not already
        exist in the database.
    """
    charset = string.ascii_lowercase + string.digits

    while True:
        length = secrets.choice(range(min_length, max_length + 1))
        slug = ''.join(secrets.choice(charset) for _ in range(length))

        if not URL.objects.filter(slug=slug).exists():
            return slug
