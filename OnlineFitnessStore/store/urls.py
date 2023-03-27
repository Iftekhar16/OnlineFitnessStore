from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='langdingpage'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('blog', views.blog, name='blog'),
    path('blogpage', views.blogpage, name='blogpage'),
    path('cart', views.cart, name='cart'),
    path('feedback', views.feedback, name='feedback'),
    # path('landingpage', views.landingpage, name='landingpage'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
]