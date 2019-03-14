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
    # 订单列表
    url(r'orderlist/$', views.orderlist, name='orderlist'),
    # 订单详情
    url(r'^orderdetail/(?P<identifier>[\d.]+)/$', views.orderdetail, name='orderdetail'),


    # 测试接口
    url(r'^randomtest/$', views.randomtest, name='randomtest'),
    # 支付成功后，客户端的显示
    url(r'^returnurl/$', views.returnurl, name='returnurl'),
    # 支付成功后，订单的处理
    url(r'^appnotifyurl/$', views.appnotifyurl, name='appnotifyurl'),
    # 支付
    url(r'^pay/$', views.pay, name='pay'),
]

