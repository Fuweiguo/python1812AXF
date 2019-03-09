import hashlib
import random

import time
from django.core.cache import cache
from django.shortcuts import render, redirect

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

    cache.set('response',response_dir,60)
    response = cache.get('response')

    return render(request,'home/home.html',context=response_dir)


#
def market(request,childcid='0',sortid='0'):
    childcid = str(childcid)
    #分类信息
    foodtypes = Foodtype.objects.all()

    #商品信息
    #默认打开　热销榜
    #点击左侧分类　　即显示对应分类　商品信息
    #【】
    # goods_list = Goods.objects.filter(categoryid=categoryid)




    #客户端　需要记录　点击分类下标　【cookie　会自动携带】
    index = int(request.COOKIES.get('index','0'))

    #根据index 获取　对应的分类
    categoryid = foodtypes[index].typeid


    #子分类
    if childcid == '0':
        # 根据　分类ＩＤ　获取对应分类信息
        goods_list = Goods.objects.filter(categoryid=categoryid)
        print( 'MMMMM　　进 0　MMMMMMMM',goods_list.count())
    else:
        # 根据　分类ＩＤ　获取对应分类信息
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childcid)
        print( 'MMMMM　　进 1　MMMMMMMM',goods_list.count())


        # 排序
        # 0默认综合排序   1销量排序     2价格最低   3价格最高

    if sortid == '1':
        goods_list = goods_list.order_by('-productnum')

    elif sortid == '2':
        goods_list = goods_list.order_by('price')

    elif sortid == '3':
        goods_list = goods_list.order_by('-price')

    print('========', 'YYY　出　　YYY',goods_list.count())
    #获取子类信息
    childtypename = foodtypes[index].childtypenames
    #将对应的子类拆分出来
    childtype_list = []

    # suclass_id = int(request.COOKIES.get('subclass'))
    # print(suclass_id)



    for item in childtypename.split('#'):
        #item >> 全部分类：０
        #item >> 子类名称：　子类ＩＤ
        item_arr = item.split(':')
        temp_dir = {
            'name':item_arr[0], #子类名称
            'id':item_arr[1], #id
        }

        childtype_list.append(temp_dir)

    # childcid = childtype_list[0]['id']
    # print(childcid)

    # suclass_goods = Goods.objects.filter(childcid=childcid)







    response_dir = {
        #
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'childtype_list':childtype_list,
        'childcid':childcid,
    }

    return render(request,'macket/macket.html',context=response_dir)

#
def cart(request):
    return render(request,'cart/cart.html')


#
def mine(request):

    token = request.session.get('token')

    user_id = cache.get(token)
    print(user_id)
    user = None
    if user_id:
        user = User.objects.get(pk = user_id)

    print(user)

    return render(request,'mine/mine.html',context={'user':user})


def login(request):
    if request.method == 'GET':
        return render(request,'mine/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email)
        if user:
            if user.last().password == password:
                user = user.last()
                token = random_token()

                cache.set(token,user.id,60*3)
                request.session['token'] = token

                return redirect('axf:mine')
            else:
                return render(request,'mine/login.html',context={
                    'err_password':'密码错误'
                })

        else:
            return render(request ,'mine/login.html',context={'err_email':'邮箱错误'})



def logout(request):
    request.session.flush()

    return render(request,'mine/mine.html')

def random_token():
    token = str(random.random()) + str(time.time())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()


def random_password():
    user = str(random.random) + str(time.time())
    md5 = hashlib.md5()
    md5.update(user.encode('utf-8'))
    return md5.hexdigest()



def register(request):
    if request.method == 'GET':
        print('aaaaaaaaa')
        return  render(request,'mine/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        rank = request.POST.get('rank')

        user = User()
        user.email = email
        user.password = password
        user.name = name
        # user.img = img
        # user.rank = rank
        user.save()

        token = random_token()

        cache.set(token,user.id,60*3)

        request.session['token']=token

        # img = request.POST.get('img')
        # print(img)
        return redirect('axf:mine')