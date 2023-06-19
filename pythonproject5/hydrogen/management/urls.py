from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('management_home1/', views.manage_1_home),
    path('management_register/', views.management_register),
    path('management_login/', views.management_login),
    path('CLI_login-APPROVE/', views.CLIENT_APPRO),
    path('login_approve_button/<int:id>/', views.client_loginapproval_button),

]
