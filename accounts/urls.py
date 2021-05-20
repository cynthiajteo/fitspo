from django.urls import path
from accounts.views import *

urlpatterns = [
    # path('register/', register_view, name='register'),
    # path('login/', login_view, name='login'),
    # path('private/', private_view, name='private'),
    # path('user/', user_data_view, name='user'),
    path('logout/', logout, name='logout')
]
