from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from app.models import URL


class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'slug', 'created_at')
    search_fields = ('original_url', 'slug')
    ordering = ('-created_at',)

    def get_queryset(self, request: HttpRequest) -> QuerySet[URL]:
        """
        Retrieves and returns a filtered QuerySet of URLs based on the
        requesting user, prefetching the related 'user' field.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            QuerySet[URL]: A QuerySet of URLs, prefetching the related 'user'
            field.
        """
        return super().get_queryset(request).prefetch_related('user')

    def user(self, obj: URL) -> str:
        """
        Retrieves and returns the email of the user associated with the URL.

        Args:
            obj (URL): The URL object.

        Returns:
            str: The email of the user associated with the URL.
        """
        return obj.user.email

    user.short_description = 'User'


admin.site.register(URL, URLAdmin)
