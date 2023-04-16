from django.shortcuts import render, get_object_or_404

# Create your views here.
from haminjory.models import Article


def home(request):
    objects = Article.objects.filter(status='d')

    context = {
        'objects': objects
    }
    return render(request, 'haminjory/list.html', context)


def detail(request, slug):

    context = {
        'object': get_object_or_404(Article,slug=slug)

    }

    return render(request, 'haminjory/detail.html', context)
