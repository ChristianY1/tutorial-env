from unicodedata import name
from django.urls import path
from .views import BlogListView, BlogCreateView, BlocDetailView, BlocUpdateView, BlocDeleteView

app_name="blogs"

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlocDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', BlocUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlocDeleteView.as_view(), name='delete')
    
]