from django.urls import path
from .views import blog, blogPost

urlpatterns = [
    path('all/', blog, name='blogs'),
    path('<str:slug>/', blogPost, name='blogpost'),
]
