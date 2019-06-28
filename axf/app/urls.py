from django.contrib import admin
from django.urls import path
from app.views import *
app_name = 'app'
urlpatterns = [
    path('home/',home,name='home'),
    path('market/<zid>/<cid>/<sortid>/',market,name='market'),
    path('cart/',cart,name='cart'),
    #修改购物车
    path('changecart/<flag>/',changecart,name='changecart'),

    #下订单
    path('saveorder/',saveorder,name='saveorder'),


    path('mine/',mine,name='mine'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    #验证账号是否被注册
    path('checkuserid/',checkuserid,name='checkuserid'),

    path('quit/',quit,name='quit')

]
