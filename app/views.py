from django.shortcuts import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    get_object_or_404,
    redirect,
    render,
)

from app.forms import URLForm
from app.models import URL
from app.utils import generate_slug


def index(request) -> HttpResponse:
    print(type(request))
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
    request, slug: str
) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    print(type(request))
    url = get_object_or_404(URL, slug=slug)
    return redirect(url.original_url)
