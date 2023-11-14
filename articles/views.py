from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    ordering = ['-id']
    paginate_by = 5

class ArticleDetailView(DetailView): 
    model = Article
    template_name = "article_detail.html"