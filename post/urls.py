from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ViewPost),
    path('all/', views.ViewAllPosts),
    path('add/', views.AddPost),
    path('update/<int:pk>/', views.UpdatePost),
    path('delete/<int:pk>/', views.DeletePost),
]
