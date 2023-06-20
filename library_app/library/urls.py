from django.urls import path
from . import views

urlpatterns = [
    path('find_book/', views.FindBookView.as_view(), name='find_book'),
    path('shelves/', views.ShelvesView.as_view(), name='shelves'),
]
