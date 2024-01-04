from django.urls import path
from .views import notebook_list


urlpatterns = [
    path('', notebook_list, name='notebook_list')
]
