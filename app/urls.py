from django.contrib.auth import logout
from django.urls import path

from app.views import *
urlpatterns = [
    path('', index, name='index'),

    path('rooms/', rooms, name='rooms'),
    path('restaurant/', restaurant, name='restaurant'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/<int:blog_id>', blog_detail, name='blog-detail'),
    path('contact/', contact, name='contact'),
    path('room-detail/<int:room_id>', room_detail, name='room-detail'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('comment/<int:blog_id>/', new_comment, name='new-comment'),
]