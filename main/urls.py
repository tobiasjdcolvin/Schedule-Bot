from django.urls import path
from .views import index_view, add_view, generate_view, delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add', add_view.as_view(), name='add'),
    path('delete', delete_view, name='delete'),
    path('generate', generate_view, name='generate'),
]
