from unicodedata import name
from django.urls import path
from .views import BlogListView, BlogCreateView

app_name="blogs"

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create')
    
]