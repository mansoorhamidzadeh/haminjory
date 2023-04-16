from django.urls import path
from . import views
app_name='haminjory'
urlpatterns=[
    path('',views.home,name='home'),
    path('artcile/<slug:slug>/',views.detail,name='detail')
]