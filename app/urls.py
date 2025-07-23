from django.urls import path
from app.views import AcrticleCreateView, ArticleListView, AcrticleUpdateView, AcrticleDeleteView

urlpatterns = [
    path('',  ArticleListView.as_view() , name='home'),
    path('create/', AcrticleCreateView.as_view(), name='create_article'),
    path('<int:pk>/update', AcrticleUpdateView.as_view(), name='update_article'),
    path('<int:pk>/delete', AcrticleDeleteView.as_view(), name='delete_article'),
]
