from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from haminjory.models import Article
# Create your views here.
class ArticleAPIList(generics.ListAPIView):
    queryset = Article.objects.publish()
    serializer_class = ArticleSerializer