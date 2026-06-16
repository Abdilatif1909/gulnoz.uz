from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='list'),
    path('create/', views.NewsCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.NewsDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.NewsUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', views.NewsDeleteView.as_view(), name='delete'),
]
