from django.urls import path
from .views import *

app_name = "posts"

urlpatterns = [
    path('', view_index, name='all_posts'),
    path('search', view_search, name='search_result'),
    path('create/', view_create, name='post_create'),
    path('likes/', view_user_likes, name='user_likes'),
    path('like/<uuid:pk>/', view_like, name='post_like'),
    path('edit<uuid:pk>/', view_post, name='post_edit'),
    path('post<uuid:pk>/', view_show_post, name='post_show'),
    path('comments/<uuid:pk>/', views_create_comment, name='comment_create'),
]
