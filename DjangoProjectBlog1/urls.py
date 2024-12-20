"""
URL configuration for DjangoProjectBlog1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 文章应用的网页路径
    path('article/', include('article.urls', namespace='article')),
    # 文章应用的API路径
    path('api/article/', include('article.urls', namespace='api_article')),
    # REST framework的认证相关路径
    path('api-auth/', include('rest_framework.urls')),
]
