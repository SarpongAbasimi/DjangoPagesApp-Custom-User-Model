from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from .models import Articles
from django.urls import reverse_lazy

# Create your views here.
class ArticleListView(ListView):
    model = Articles
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Articles
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model =Articles
    template_name ='article_delete.html'
    success_url=reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self,request, *args, **kwargs):
        obj=self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        else:
            return super().dispatch(request,*args,**kwargs)


class ArticleUpdateView(LoginRequiredMixin,UpdateView):
    model=Articles
    fields= ('title','content')
    template_name='article_edit.html'
    login_url = 'login'

    def dispatch(self,request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied 
        else:
            return super().dispatch(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title', 'content',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)