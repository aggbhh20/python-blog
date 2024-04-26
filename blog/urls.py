from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("fuckyou", views.fuckyou, name="fuckyou"),
    path("todos/", views.todos, name="todos"),
    path("blogposts/", views.blogposts, name="blogposts"),
    path("deleteBlogpost/", views.deleteBlogpost, name="deleteBlogpost"),
    path("seeBlogposts/", views.seeBlogposts, name="seeBlogposts")
]
