from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.ViewPost),
    path('all/', views.ViewAllPosts),
    path('add/', views.AddPost),
    path('update/<int:id>/', views.UpdatePost),
    path('delete/<int:id>/', views.DeletePost),
]
