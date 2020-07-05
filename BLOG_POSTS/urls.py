from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('article/<int:pk>/', views.PostList.as_view(), name='postlist'),
    path('article/new/', views.PostForm.as_view(), name='postform'),
    path('article/edit/<int:pk>/', views.PostEdit.as_view(), name='postedit'),
    path('article/<int:pk>/delete/', views.PostDelete.as_view(), name='postdelete'),
]