from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^market/$',views.market,name='marketbase'),#闪购超市
url(r'^market/(?P<childcid>\d+)/(?P<sortid>\d+)/$',views.market,name='market'),#闪购超市
    #购物车
    url(r'^cart/$',views.cart,name='cart'),
    #我的
    url(r'^mine/$',views.mine,name='mine'),
    #登录
    url(r'^login/$',views.login,name='login'),
    #退出
    url(r'^loginout/$', views.logout, name='logout'),
    #注册
    url(r'^register/$', views.register, name='register'),


    #账号验证
    url(r'^checkemail/$',views.checkemail,name='checkemail'),
    url(r'^addcart/$',views.addcart,name='addcart'),

]

