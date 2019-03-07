from django.core.cache import cache
from django.shortcuts import render

#
from axf.models import *


def home(request):



    print('aaaaaaa')

    # 轮播图
    wheel = Wheel.objects.all()
    print('bbbbbbb')

    nav = Nav.objects.all()

    mustbuy = Mustbuy.objects.all()

    shops = Shop.objects.all()
    shopheab = shops[0]
    shoptabs = shops[1:3]

    shopclass_list = shops[3:7]

    goods = shops[7:11]
    print('cccccccc')
    mainshows = Mainshow.objects.all()


    response_dir = {
        'wheel':wheel,
        'nav':nav,
        'mustbuy':mustbuy,
        'shophead':shopheab,
        'shopheas':shoptabs,
        'shopclass_list':shopclass_list,
        'goods':goods,
        'mainshows':mainshows,

    }
    print('dddddd')

    cache.set('response',response_dir,60)
    response = cache.get('response')

    return render(request,'home/home.html',context=response_dir)


#
def market(request):
    foodtypes = Foodtype.objects.all()
    goods_list = Goods.objects.first()

    response_dir = {
        'foodtypes': foodtypes,
        'goods_list': goods_list,
    }

    return render(request,'macket/macket.html',context=response_dir)

#
def cart(request):
    return render(request,'cart/cart.html')

#
def mine(request):
    return render(request,'mine/mine.html')