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
    print(response)

    return render(request,'home/home.html',context=response_dir)


#
def market(request):
    #分类信息
    foodtypes = Foodtype.objects.all()

    #商品信息
    #默认打开　热销榜
    #点击左侧分类　　即显示对应分类　商品信息
    #【】
    # goods_list = Goods.objects.filter(categoryid=categoryid)


    #客户端　需要记录　点击分类下标　【cookie　会自动携带】
    index = int(request.COOKIES.get('index','0'))
    print(index,'ppppppppppppp')
    #根据index 获取　对应的分类
    categoryid = foodtypes[index].typeid
    #根据　分类ＩＤ　获取对应分类信息
    goods_list = Goods.objects.filter(categoryid=categoryid)

    #获取子类信息
    childtypename = foodtypes[index].childtypenames
    #将对应的子类拆分出来
    childtype_list = []

    for item in childtypename.split('#'):
        #item >> 全部分类：０
        #item >> 子类名称：　子类ＩＤ
        item_arr = item.split(':')
        temp_dir = {
            'name':item_arr[0],
            'id':item_arr[1],

        }

        childtype_list.append(temp_dir)

    response_dir = {
        #
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'childtype_list':childtype_list,
    }

    return render(request,'macket/macket.html',context=response_dir)

#
def cart(request):
    return render(request,'cart/cart.html')

#
def mine(request):
    return render(request,'mine/mine.html')