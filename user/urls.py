from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.ViewUser),
    path('all/', views.ViewAllUsers),
    path('add/', views.AddUser),
    path('update/<int:pk>/', views.UpdateUser),
    path('delete/<int:pk>/', views.DeleteUser),
    path('import-csv/', views.ImportCsv),
]
