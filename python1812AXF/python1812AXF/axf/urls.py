from django.conf.urls import url

from axf import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^market/$',views.market,name='marketbase'),#闪购超市

    url(r'^cart/$',views.cart,name='cart'),#购物车
    url(r'^mine/$',views.mine,name='mine'),#我的

    url(r'^market/(?P<childcid>\d+)/(?P<sortid>\d+)/$',views.market,name='market'),#闪购超市
    url(r'^login/$',views.login,name='login'),
    url(r'^loginout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]

