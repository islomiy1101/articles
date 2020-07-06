from django.shortcuts import render
from .models import Aricle
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

def article_list(request):
    articles=Aricle.objects.all()
    return render(request,'articles/article_list.html',{'articles':articles})



def article_detail(request,slug):
    article=get_object_or_404(Aricle,slug=slug)
    # article=Aricle.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})