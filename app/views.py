from django.shortcuts import render
from app.models import ArticleData
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = ArticleData
    template_name = 'app/home.html'
    context_object_name = 'articles'

class AcrticleCreateView(CreateView):
    model = ArticleData
    fields = ['title', 'content', 'twitter_post', 'status']
    template_name = 'app/article_create.html'
    success_url = reverse_lazy('home')
    
class AcrticleUpdateView(UpdateView):
    model = ArticleData
    fields = ['title', 'content', 'twitter_post', 'status']
    template_name = 'app/article_update.html'
    success_url = reverse_lazy('home')
    context_object_name = "article"
    
class AcrticleDeleteView(DeleteView):
    model = ArticleData
    template_name = 'app/article_delete.html'
    success_url = reverse_lazy('home')
    context_object_name = "article"

