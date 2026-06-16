from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('my-dashboard/', views.my_dashboard, name='my_dashboard'),
    path('reports/system/', views.system_report_pdf, name='system_report_pdf'),
]
