from django.urls import path, include
from .views import HomePage, redirect_view, PostsView, DetailPage, CreatePost, ChangePost

urlpatterns = [
    path("home/", HomePage.as_view(), name="home_page"),
    path("", redirect_view, name="redirect"),
    path("posts/", PostsView.as_view(), name="posts_page"),
    path("detail/<int:id>/", DetailPage.as_view(), name="detail_page"),
    path("create_post/", CreatePost.as_view(), name="create_post_page"),
    path("change_post/<int:id>", ChangePost.as_view(), name="change_post_page")
]