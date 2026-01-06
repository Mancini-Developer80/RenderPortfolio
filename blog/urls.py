from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='home'),
    path('search/', views.blog_search, name='search'),
    path('tag/<slug:slug>/', views.tag_posts, name='tag_posts'),
    path('<slug:slug>/', views.blog_detail, name='detail'),
]

