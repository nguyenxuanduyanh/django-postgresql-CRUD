from django.urls import path
from . import views
urlpatterns = [
    path('<int:id>/', views.ViewUser),
    path('all/', views.ViewAllUsers),
    path('add/', views.AddUser),
    path('update/<int:id>/', views.UpdateUser),
    path('delete/<int:id>/', views.DeleteUser),
]
