from django.shortcuts import render

# Create your views here.
# article/views.py

from django.http import JsonResponse
from article.models import Article
# 这个 ArticleListSerializer 暂时还没有
from article.serializers import ArticleListSerializer
from django.shortcuts import render, get_object_or_404
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)