from django.urls import path
from todolist.tarefas import views

app_name = 'tarefas'
urlpatterns = [
    path('', views.home, name='home'),
]
