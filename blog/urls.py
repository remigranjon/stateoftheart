from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('newArticle/', views.newArticle, name='newArticle'),
    path('save/', views.saveArticle, name='saveArticle'),
    path('<int:article_id>/update/', views.updateArticle, name="updateArticle"),
    path('<int:article_id>/delete/', views.deleteArticle, name="deleteArticle"),
    path('<int:article_id>/writeComment/', views.writeComment, name="writeComment"),
    path('uploadImage/', views.uploadImage, name="uploadImage"),
    path('deleteComment/', views.deleteComment, name="deleteComment"),
    path('search/',views.searchArticle, name="search"),
    ]