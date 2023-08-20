from django.urls import path, include
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='LogIn'),
    path('logout_user', views.logout_user, name='LogOut'),
    path('register_user', views.register_user, name='RegisterUser'),
    path('profile_page', views.profile_page, name='ProfilePage'),
    path('registration_successful', views.registration_success, name='registration_successful'),
    
    # path('', include('main.urls'))
]
