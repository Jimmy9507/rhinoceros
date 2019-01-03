from django.shortcuts import render
from django.http import HttpResponse
from . import models

def homepage(request):
    articles=models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})

def index(request):
    #article=models.Article.objects.get(pk=1) #返回 主键为1的对象
    articles=models.Article.objects.all() #Django 返回的一个集合列表
    return render(request, 'blog/index.html', {'articles':articles})


# Create your views here.
def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':article})


def about(request):
    return render(request,'blog/about.html')


def hotel(request):
    return render(request,'blog/hotel.html')


def places(request):
    return render(request,'blog/places.html')


def contact(request):
    return render(request,'blog/contact.html')


def blog_show(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/blog_show.html',{'articles':articles})


def blog_single(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/blog_single.html', {'article':article})


def edit_page(request,article_id):
    if str(article_id)=='0':
        return render(request, 'blog/edit_page.html')
    article=models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article':article})


def edit_action(request):
    title = request.POST.get('title', 'CONTENT')
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')
    if article_id =='0':
        models.Article.objects.create(title=title,content=content)
        articles=models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles':articles})
    article=models.Article.objects.get(pk=article_id)
    article.title=title
    article.save()
    article.content=content
    article.save()
    return render(request, 'blog/article_page.html', {'article':article})