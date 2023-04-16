from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from haminjory.models import Article, Category


class ArticleList(ListView):
    context_object_name = 'objects'
    queryset = Article.objects.publish()
    template_name = 'haminjory/list.html'


class ArticleDetail(DetailView):
    template_name = 'haminjory/detail.html'
    context_object_name = 'object'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug)


class CategoryList(ListView):
    context_object_name = 'article'
    template_name = 'haminjory/category.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.publish()
#
# def home(request):
#     objects = Article.objects.publish()
#
#     context = {
#         'objects': objects
#     }
#     return render(request, 'haminjory/list.html', context)

# def detail(request, slug):
#     context = {
#         'object': get_object_or_404(Article, slug=slug)
#
#     }
#
#     return render(request, 'haminjory/detail.html', context)
# def category(request, slug):
#     category = get_object_or_404(Category, slug=slug, status=True)
#     article_list = category.articles.publish()
#     context = {
#         "article": article_list
#     }
#
#     return render(request, 'haminjory/category.html', context)
