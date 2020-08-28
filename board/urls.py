from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('index/', views.index),
    path('', views.index),
    
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('article/write/', views.write),
    path('article/list/', views.list),
    path('article/detail/<int:id>/', views.detail),
    path('article/update/<int:id>/', views.update),
    path('article/delete/<int:id>/', views.delete),
    
    path('map/', views.map),
    path('map_data/', views.map_data),
    
    path('contact/', views.contact),
    
    path('upload/', views.upload),
    
    path('test/', views.test),
]
