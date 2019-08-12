from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # directs user to index when no path
    path('about', views.about, name='about'), # directs user to about page when /about
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('test', views.dep, name='test'),
    # path('test', views.dep, name='search'),
    path('dep', views.dep, name='register'),
    path('login', views.login, name='login'),
    path('ip/', views.ip, name='ip'),
]
