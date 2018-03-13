from django.conf.urls import url
from . import views


app_name = 'weibo'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^homepage/', views.homepage, name='homepage'),
    #url(r'^update/', views.update, name='update'),
    url(r'^userpage/', views.user_page, name='userpage'),
    url(r'^follow', views.user_follow, name='follow'),
    url(r'^unfollow', views.user_unfollow, name='unfollow'),
]
