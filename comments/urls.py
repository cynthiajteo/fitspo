from django.urls import path
from comments.views import *


app_name = 'comments'

urlpatterns = [
    path('<uuid:post>', views_create, name='comment_create'),
    #  path("", views.views_index, name='reviews_index')
    # path("<uuid:post_id>", view_reviews, name='reviews_index')
]
