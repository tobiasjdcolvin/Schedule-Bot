from django.urls import path
from .views import index_view, add_view, generate_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add', add_view, name='add'),
    path('generate', generate_view, name='generate'),
]
