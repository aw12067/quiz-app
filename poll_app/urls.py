from django.contrib import admin
from django.urls import path
from poll import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),    
    path('create/', views.create, name='create'),
    path('check/<poll_id>/', views.check, name='check'),
    path('result/', views.result, name='result'),
    path('clear/', views.clear, name='clear'),
    path('test/', views.test, name='test')
]
