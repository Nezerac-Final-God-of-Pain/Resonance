from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name=""),
  path('login', views.login, name="login"),
  #path('store', views.store, name="store"),
  path('register', views.register, name="register"),
  path('logout', views.logout, name="logout"),
  path('dashboard',views.dashboard, name="dashboard")
]
