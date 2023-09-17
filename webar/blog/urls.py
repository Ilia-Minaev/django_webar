"""
URL configuration for webar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from blog.views import HomeView, HomeRedirectView, PageView, ArticlesView, ArticleSingleView, AboutView, ServicesView, ContactView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('home/', HomeRedirectView.as_view(), name='home_redirect'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', ArticlesView.as_view(), name='articles'),
    path('blog/<slug:article_slug>/', ArticleSingleView.as_view(), name='article-single'),
    path('<slug:page_slug>/', PageView.as_view() , name='page'),
]