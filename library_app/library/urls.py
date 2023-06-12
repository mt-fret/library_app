from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('shelves/', views.ShelvesView.as_view(), name='shelves'),
]