from django.urls import path
from .views import home_page_view, add_img_url

urlpatterns = [
    path('', home_page_view, name='home'),
    path('add_img_url', add_img_url, name='add_img_url'),
]
