from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/pics/<int:note_id>/', views.api_pic_get),
    path('api/pics/',views.api_pic_post)
]