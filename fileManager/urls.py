from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>/create', views.create, name='create'),
    path('<str:id>/delete',views.delete, name='delete'),
    path('<str:id>/download',views.download, name='download')
]