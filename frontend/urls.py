from django.urls import path
from frontend import views

urlpatterns = [
    path('list',views.list,name='list')
]