from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/detail/', views.book_detail, name="book_detail"),
    path('<int:book_id>/checkout/', views.checkout, name='checkout'),
    path('<int:book_id>/return_book/', views.return_book, name='return_book'),
]