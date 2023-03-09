from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book-search/', views.search, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail')
]
