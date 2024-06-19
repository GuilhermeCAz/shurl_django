import yaml
from django.http.request import HttpRequest
from django.http.response import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import get_object_or_404, redirect, render

from app.forms import URLForm
from app.models import URL
from app.utils import generate_slug
from shurl_django.settings import BASE_DIR


def docs(request: HttpRequest) -> HttpResponse:
    """
    Retrieves the OpenAPI specification from a YAML file and returns it as a
    JSON response.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the OpenAPI
        specification as JSON.
    """
    with open(BASE_DIR / 'openapi.yaml') as f:
        spec = yaml.safe_load(f)

    return JsonResponse(spec)


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


def redirect_to_original(
    request: HttpRequest, slug: str
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
