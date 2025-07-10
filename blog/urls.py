from blog.views import BlogPostDetailView, BlogPostListView
from django.urls import path


urlpatterns = [
    path('<slug:slug>', BlogPostDetailView.as_view(), name='post_detail'),
    path('', BlogPostListView.as_view(), name='post_list')

]