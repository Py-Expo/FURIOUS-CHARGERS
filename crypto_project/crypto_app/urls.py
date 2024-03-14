
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('encrypt/', views.encrypt_file, name='encrypt_file'),
    path('decrypt/', views.decrypt_file, name='decrypt_file'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]

