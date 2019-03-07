from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^market/$',views.market,name='markert'),#闪购超市
    url(r'^cart/$',views.cart,name='cart'),#购物车
    url(r'^mine/$',views.mine,name='mine'),#我的

]