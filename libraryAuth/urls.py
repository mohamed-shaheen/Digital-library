from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views




app_name = 'libraryAuth'





urlpatterns = [
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('signup/', views.signup, name='signup'),
]