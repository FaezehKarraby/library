from django.urls import path

from account import views

urlpatterns = [
    path('', views.SignupView.as_view(), name='signup'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('my_books/<int:id>', views.my_books, name='my_books'),
]