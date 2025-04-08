from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('servicing/', views.service, name="service"),
    path('blog/', views.blog, name="blog"),
    path('pricing/', views.price, name="price"),
]
