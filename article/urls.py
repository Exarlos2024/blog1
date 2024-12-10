# 引入path
from django.urls import path
from article import views
# 正在部署的应用的名称
app_name = 'article'

urlpatterns = [
    # 网页视图
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),

    # API视图，使用rest_framework的viewsets或views
    path('api/list/', views.ArticleListView.as_view(), name='api_article_list'),
    path('api/detail/<int:pk>/', views.ArticleDetailView.as_view(), name='api_article_detail'),
]