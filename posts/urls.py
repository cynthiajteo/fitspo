from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', view_index, name='all_posts'),
    path('create/', view_create, name='post_create'),
    path('edit<uuid:pk>/', view_post, name='post_edit'),
    path('post<uuid:pk>', view_show_post, name='post_show'),
]
