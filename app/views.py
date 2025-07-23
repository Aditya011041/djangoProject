from django.shortcuts import render
from app.models import ArticleData
from django.views.generic import CreateView
from django.urls import reverse_lazy


def home(request):
    article = ArticleData.objects.all()
    return render(request , 'app/home.html' , {"article":article})

class AcrticleCreateView(CreateView):
    model = ArticleData
    fields = ['title', 'content', 'word_counts', 'twitter_post', 'status']
    template_name = 'app/article_create.html'
    success_url = reverse_lazy('home')