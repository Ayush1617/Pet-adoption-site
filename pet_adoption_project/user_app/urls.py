from django.urls import path
from . import views
app_name= 'user_app'


urlpatterns = [
 path('register/',views.user_register, name = 'user_registration' ),
 path('user_login/',views.user_login, name = 'user_login' ),
 path('dashboard/',views.dashboard, name = 'dashboard' ),
 path('logout/',views.user_logout, name = 'user_logout' ),

]