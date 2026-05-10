from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Home
    path('', views.dashboard_home, name='home'),

    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('categories/<int:pk>/merge/', views.category_merge, name='category_merge'),

    # Products
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # Blog Posts
    path('blog/posts/', views.blog_post_list, name='blog_post_list'),

    path('blog/posts/add/', views.blog_post_add, name='blog_post_add'),
    path('blog/posts/<int:pk>/edit/', views.blog_post_edit, name='blog_post_edit'),
    path('blog/posts/<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),

    # Contact Messages
    path('messages/', views.contact_messages, name='contact_messages'),
    path('messages/<int:pk>/delete/', views.contact_message_delete, name='contact_message_delete'),

]
