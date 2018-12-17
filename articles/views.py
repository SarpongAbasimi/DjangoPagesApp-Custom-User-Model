from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from .models import Articles
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'

class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'


class ArticleDeleteView(DeleteView):
    model =Articles
    template_name ='article_delete.html'
    success_url=reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model=Articles
    fields= ('title','content')
    template_name='article_edit.html'