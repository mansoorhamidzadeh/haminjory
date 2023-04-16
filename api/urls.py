from django.urls import path
from . import views
urlpatterns=[
    path('',views.ArticleAPIList.as_view())
]