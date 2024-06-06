from django.db import models


class URL(models.Model):
    original_url = models.URLField()
    slug = models.CharField(max_length=10, unique=True)
    date_generated = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.slug} -> {self.original_url}'
