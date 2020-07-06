from django.conf.urls import url
from . import views
from django.urls import path

app_name='articles'
urlpatterns=[
    url('',views.article_list,name='list'),
    path('article/detail/<str:slug>', views.article_detail, name='article'),
    # url('/<str:slug>',views.article_deta)
    # url('(?P<slug>[\w-]+)/',views.article_detail,name='detail')
]