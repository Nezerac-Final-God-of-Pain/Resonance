from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name=""),
  path('login', views.login, name="login"),
  #path('store', views.store, name="store"),
  path('register', views.register, name="register"),
  path('logout', views.logout, name="logout"),
  path('dashboard',views.dashboard, name='dashboard'),
  path('create_record', views.create_record, name="create_record"),
  path('update_record/<int:pk>', views.update_record, name="update_record" ),
  path('record/<int:pk>', views.singular_record, name="record"),
  path('delete_record/<int:pk>', views.delete_record, name="delete_record"),
]
