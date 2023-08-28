from django.urls import path
from .views import index,top_sellers,advertisement_post,advertisement,profile,register,login
urlpatterns = [

    path('',index,name = 'main-page'),
    path('top-sellers/',top_sellers,name = 'top-sellers'),
    path('advertisement-post/',advertisement_post,name = 'adv-post'),
    path('advertisement/',advertisement,name = 'advertisement'),
    path('profile/',profile,name = 'profile'),
    path('register/',register,name = 'register'),
    path('login/',login,name = 'login'),
]