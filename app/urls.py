from django.urls import path
from app.views import home, AcrticleCreateView

urlpatterns = [
    path('',  home , name='home'),
    path('articles/create/', AcrticleCreateView.as_view(), name='create_article'),
]
