# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from blog.models import Column,Article


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)

    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'blog/column.html', {'column': column})


def article_detail(request, pk,article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)


    return render(request, 'blog/article.html', {'article': article})
# Create your views here.
