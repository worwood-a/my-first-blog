from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('cv/', views.cv, name='cv'),
    path('cv/edit/<str:form_title>', views.cv_new, name='cv_new'),
    path('cv/edit/<str:form_title>/<int:pk>', views.cv_edit, name='cv_edit')
]