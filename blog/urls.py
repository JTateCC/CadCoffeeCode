from blog.views import BlogPostDetailView, BlogPostListView
from django.urls import path


urlpatterns = [
    path('<slug:slug>', BlogPostDetailView.as_view(), name='blog_detail'),
    path('', BlogPostListView.as_view(), name='blog_list')

]