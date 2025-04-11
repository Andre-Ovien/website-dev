from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.authlogin, name="login"),
    path('register/',views.authregistration, name="register"),
    path('password-reset/',views.authreset, name="reset"),
    path('logout/',views.authlogout, name="logout")
]
