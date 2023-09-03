from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Category

# Create your views here.

class Home(ListView):
    model = Category
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'title'
        return context
    