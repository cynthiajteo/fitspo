from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('register/', views_register, name="register"),
    path('login/', views_login, name="login"),
    path('logout/', views_logout, name="logout"),
    path('profile/<user_id>/', views_profile, name="profile_show"),
    # path('profile/<user_id>/', views_others, name="profile_show"),

]
