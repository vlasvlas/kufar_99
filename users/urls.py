from django.urls import path
from .views import login, SignUp

urlpatterns = [
    path('login', login, name='login'),
   # path('logout', login, name='logout'),
    path('register', SignUp.as_view(), name='register'),
]
