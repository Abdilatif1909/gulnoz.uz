from django.urls import path

from . import views

app_name = 'investments'

urlpatterns = [
    path('', views.InvestmentListView.as_view(), name='list'),
    path('export/csv/', views.export_investments_csv, name='export_csv'),
    path('create/', views.InvestmentCreateView.as_view(), name='create'),
    path('<int:pk>/', views.InvestmentDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.InvestmentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.InvestmentDeleteView.as_view(), name='delete'),
    path('<int:pk>/apply/', views.InvestorApplicationCreateView.as_view(), name='apply'),
]
