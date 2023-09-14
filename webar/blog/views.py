from typing import Any, Optional
from django.shortcuts import render
from django.views.generic import ListView, RedirectView
from django.urls import reverse_lazy

from blog.models import Page
from blog.utils import DataMixin

# Create your views here.

class HomeView(DataMixin, ListView):
    model = Page
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        self.kwargs['slug'] = 'home'
        context = super().get_context_data(**kwargs)
        context_mixin = self.get_user_base_context()
        context = context | context_mixin
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
        context_mixin = self.get_user_base_context()
        context = context | context_mixin
        return context