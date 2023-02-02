"""homework1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from myapp.views import main, my_arcticles, arct_archive, users, article, regexp, symbol
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('arcticles/', my_arcticles),
    path('arcticles/archive/', arct_archive, name='arct_archive'),
    path('users/', users),

    path('article/<int:article_number>/', article, name='article_number'),
    path('article/<int:article_number>/archive/', article, name='archive_number'),
    path('article/<int:article_number>/<slug:slug_text>/', article, name='slug_text'),
    path('users/<int:user_number>/', users, name='users_number'),

    re_path(r'^([1-9a-f]{4}\-[0-9a-f]{6})/$', symbol, name='symbol'),
    re_path(r'^(0(39|67|68|96|97|98|50|66|95|99|63|73|93)\d{7})/$', regexp),

]

