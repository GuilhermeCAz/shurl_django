from django.db.models import query
from django.http.request import HttpRequest
from django.shortcuts import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    get_object_or_404,
    redirect,
    render,
)
from rest_framework import viewsets

from app.forms import URLForm
from app.models import URL
from app.serializer import URLSerializer
from app.utils import generate_slug


class URLViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the URL model.
    """

    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def get_queryset(self) -> query.QuerySet[URL]:
        """
        Retrieves and returns a filtered QuerySet of URLs based on the
        requesting user.
        """
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer: URLSerializer) -> None:
        """
        Saves the serializer with the current user as the owner.
        """
        serializer.save(user=self.request.user)


def redirect_to_original(
    request: HttpRequest,
    slug: str,
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    """
    Redirects the user to the original URL associated with a given slug.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the URL to redirect to.

    Returns:
        HttpResponseRedirect | HttpResponsePermanentRedirect: The HTTP response
        object that redirects the user to the original URL.
    """
    url = get_object_or_404(URL, slug=slug)

    return redirect(url.original_url)


def index(request: HttpRequest) -> HttpResponse:
    """
    Index view for handling both GET and POST requests.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            slug = generate_slug()
            URL.objects.create(original_url=original_url, slug=slug)
            return render(request, 'app/index.html', {'slug': slug})
    else:
        form = URLForm()

    return render(request, 'app/index.html', {'form': form})
