"""to_do_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from to_do_project.app_ToDo.views import addToDo
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app_ToDo.views import home,addToDo,deleteTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_ToDo/',home),
    path('addToDo/',addToDo),
    path('deleteTodo/<int:todo_id>/',deleteTodo)
]
