from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import (CreateView, DetailView, ListView, UpdateView, ListView, DeleteView)

from .forms import ArticleForm 

from .models import Article

# class ArticleListView(ListView):
#     queryset = Article.objects.all()
    

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = { 'form' : form }
    return render(request, "articles/article_create.html", context)

def article_detail_view(request, id): 
    obj = get_object_or_404(Article, id = id)
    context = { 'object' : obj}
    return render(request, "articles/article_detail.html", context)

def article_list_view(request): #2:58
    queryset = Article.objects.all()
    context = { 'object_list' : queryset }
    return render(request, "articles/article_list.html", context)

