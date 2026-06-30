from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('writers/', views.writers_list, name='writers'),
    path('writers/<str:name>/', views.writer_detail, name='writer_detail'),

    # Маршрут для фильтрации (задание 5)
    path('writers/', views.writers_filtered, name='writers_filtered'),

    path('books/', views.books, name='books'),
    path('books/<int:position>/', views.book_detail, name='book_detail'),
    path('book/<str:book_slug>/', views.book_by_slug, name='book_by_slug'),
]
