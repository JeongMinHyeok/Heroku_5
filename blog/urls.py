from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.home, name="home"),
    path("home/<int:blog_id>/", views.detail, name="detail"),
    path("new/", views.new, name="post_new"),
    path("edit/<int:blog_id>/", views.edit, name="edit"),
    path("delete/<int:blog_id>/", views.remove, name="delete"),
    path("comment_edit/<int:comment_id>/", views.comment_edit, name="comment_edit"),
    path("comment_delete/<int:comment_id>/", views.comment_delete, name="comment_delete"),
    path("hashtag/", views.hashtagform, name="hashtag"),
    path("search/<int:hashtag_id>", views.search, name="search"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)