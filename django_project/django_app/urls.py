from django.urls import path
from .import views
urlpatterns = [
    path('list/', views.todo_list, name='list'),
    path('create/', views.todo_create, name='create'),
    path('update/<int:pk>/', views.todo_update, name='update'),
    path('delete/<int:pk>/', views.todo_delete, name='delete'),
]