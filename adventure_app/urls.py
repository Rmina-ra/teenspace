from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name="home_page"),
    path('sign-up/', views.sign_up_page, name="sign_up_page"),
    path('profile/', views.profile_page, name="profile_page"),
    path('login/', views.login_page, name="login_page"),
    path('main/category/<slug:slug>/', views.category_by_main_page, name="category_by_main_page"),
    path('logout/', views.logout_action, name="logout_action"),
    path('place/detail/<int:pk>/', views.place_detail, name="place_detail"),
    path('search/', views.search_action, name="search_action"),
    path('create/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('register/parent/', views.register_parent, name='register_parent'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('register/child/', views.register_child, name='register_child'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/', views.complete_task, name='complete_task'),
]