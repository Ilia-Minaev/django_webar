from typing import Any, Optional
from django.shortcuts import render
from django.views.generic import ListView, RedirectView
from django.urls import reverse_lazy

from blog.models import Page, Articles
from blog.utils import DataMixin
from constants.models import Slider

# Create your views here.

class HomeView(DataMixin, ListView):
    model = Page
    template_name = 'blog/index.html'
    context_object_name = 'slider'

    def get_queryset(self):
        #context = super().get_queryset()
        slider = Slider.objects.filter(action=True)
        articles = Articles.objects.filter(action=True)[:3]
        context = {
            'slider': slider,
            'articles': articles
        }
        return slider
    

    def get_context_data(self, **kwargs):
        self.kwargs['page_slug'] = 'home'
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants
        context['articles'] = Articles.objects.filter(action=True)[:3]
        return context


class HomeRedirectView(RedirectView):
    url = reverse_lazy('home')

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        return super().get_redirect_url(*args, **kwargs)


class PageView(DataMixin, ListView):
    model = Page
    template_name = 'blog/page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants
        return context
    
class ArticlesView(DataMixin, ListView):
    model = Page
    template_name = 'blog/articles/articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        #context = super().get_queryset()
        articles = Articles.objects.filter(action=True)
        return articles

    def get_context_data(self, **kwargs):
        self.kwargs['page_slug'] = self.request.path.replace('/', '')
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants
        return context
    
class ArticleSingleView(DataMixin, ListView):
    model = Articles
    template_name = 'blog/articles/article-single.html'
    context_object_name = 'articles'

    def get_queryset(self):
        #context = super().get_queryset()
        articles = Articles.objects.get(slug=self.kwargs['article_slug'])
        return articles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_page = self.get_article_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        return context
    
class AboutView(DataMixin, ListView):
    model = Page
    template_name = 'blog/about.html'

    def get_context_data(self, **kwargs):
        self.kwargs['page_slug'] = self.request.path.replace('/', '')
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants
        
        return context
    
class ServicesView(DataMixin, ListView):
    model = Page
    template_name = 'blog/services.html'

    def get_context_data(self, **kwargs):
        self.kwargs['page_slug'] = self.request.path.replace('/', '')
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        return context
    
class ContactView(DataMixin, ListView):
    model = Page
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        self.kwargs['page_slug'] = self.request.path.replace('/', '')
        context = super().get_context_data(**kwargs)
        context_page = self.get_page_context()
        context_constants = self.get_constants()
        context = context | context_page | context_constants

        return context