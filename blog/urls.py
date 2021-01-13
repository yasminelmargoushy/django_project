from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
)
from . import views
urlpatterns = [
    path('',views.main,name='main'),
    path('blog/', PostListView.as_view(), name='blog-home'),
    path('postreview/<int:id>/',views.postreview,name='postreview'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('update_itempost/', views.updatepostitem, name="update_itempost"),
    path('password-change/',auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),name="password_change"),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name="password_change_done"),
    path('user/<str:username>/',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('profile/favorites/',user_views.favourite_list,name='favourite_list'),
    path('fav/<int:pk>/',user_views.favourite_add,name='favourite_add'),
    path('search2/', views.search, name="search2"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


