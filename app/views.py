from django.shortcuts import render
from app.models import ArticleData

# Create your views here.

def home(request):
    article = ArticleData.objects.all()
    return render(request , 'app/home.html' , {"article":article})