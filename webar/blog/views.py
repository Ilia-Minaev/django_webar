from typing import Any, Optional
from django.shortcuts import render
from django.views.generic import ListView, RedirectView
from django.urls import reverse_lazy

from blog.models import Page

# Create your views here.

class HomeView(ListView):
    model = Page
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = Page.objects.get(slug='home')
        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title
        context['meta_description'] = page.meta_description
        context['meta_keywords'] = page.meta_keywords
        return context
    
class HomeRedirectView(RedirectView):
    url = reverse_lazy('home')

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        return super().get_redirect_url(*args, **kwargs)
    
class PageView(ListView):
    model = Page
    template_name = 'blog/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = Page.objects.get(slug=self.kwargs['slug'])
        context['title'] = page.title
        context['description'] = page.description
        context['meta_title'] = page.meta_title
        context['meta_description'] = page.meta_description
        context['meta_keywords'] = page.meta_keywords
        return context