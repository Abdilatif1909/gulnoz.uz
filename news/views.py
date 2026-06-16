from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import NewsForm
from .models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'articles'
    paginate_by = 9

    def get_queryset(self):
        queryset = News.objects.all()
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_published=True)
        return queryset


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        queryset = News.objects.all()
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_published=True)
        return queryset


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/news_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'news/news_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('news:list')
