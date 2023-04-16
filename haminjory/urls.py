from django.urls import path
from . import views
app_name='haminjory'
urlpatterns=[
    path('',views.ArticleList.as_view(),name='home'),
    path('artcile/<slug:slug>/',views.ArticleDetail.as_view(),name='detail'),
    path('categoty/<slug:slug>/',views.CategoryList.as_view(),name='category')
]