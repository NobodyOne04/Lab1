from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<path:id>', views.create, name='create'),
    path('delete/<path:id>',views.delete, name='delete'),
    path('download/<path:id>',views.download, name='download'),
    path('<path:id>', views.view, name='view')
]