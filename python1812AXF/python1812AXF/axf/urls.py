from django.conf.urls import url

from axf import views

urlpatterns = [
    #主页面
    url(r'^$',views.home,name='home'),
    #商品页
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

    #加操作
    url(r'^addcart/$',views.addcart,name='addcart'),
    #减操作
    url(r'^subcart/$',views.subcart,name='subcart'),

    #修改商品选中状态
    url(r'^changecarrtselect/$',views.changecarrtselect,name='changecarrtselect'),

    #全选/取消全选
    url(r'^changecartall/$', views.changecartall, name='changecartall'),
    #生成订单
    url(r'^generateorder/$',views.generateorder,name='generateorder'),
]

