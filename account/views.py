from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from haminjory.models import Article
from .froms import ArticleCreateForm
from .mixins import FieldsMixin


class LoginView(LoginView):
    pass


class ArticleList(LoginRequiredMixin, FieldsMixin, ListView):
    queryset = Article.objects.all()
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class ArticleCreate(CreateView):
    model = Article
    template_name = 'registration/createupdate.html'
    form_class = ArticleCreateForm
