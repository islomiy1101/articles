from . import views
from django.urls import path

app_name='articles'
urlpatterns=[
    path('',views.article_list,name='list'),
    path('article/detail/<str:slug>', views.article_detail, name='article'),
]