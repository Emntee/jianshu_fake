"""jianshu_fake URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from website import views as website_view

from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', website_view.home, name='home'),
    path('collection/overview/', website_view.collections, name='collections'),
    re_path(r'^collection/(?P<collection_id>[0-9]+)/$', website_view.collection, name='collection'),
    re_path(r'^article/(?P<article_id>\d+)/$', website_view.article, name='article'),
    re_path(r'^profile/(?P<user_id>\d+)/$', website_view.user_page, name='account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
