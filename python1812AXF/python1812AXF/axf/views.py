import hashlib
import random
from urllib.parse import parse_qs

import time
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from axf.alipay import alipay
from axf.models import *


@cache_page(60 * 1, key_prefix="zyz")
def home(request):
    print('@@@@@@@@@@@@@@@@@@@@@@@')

    # 轮播图
    wheel = Wheel.objects.all()

    nav = Nav.objects.all()

    mustbuy = Mustbuy.objects.all()

    shops = Shop.objects.all()
    shopheab = shops[0]
    shoptabs = shops[1:3]

    shopclass_list = shops[3:7]

    goods = shops[7:11]
    mainshows = Mainshow.objects.all()

    response_dir = {
        'wheel': wheel,
        'nav': nav,
        'mustbuy': mustbuy,
        'shophead': shopheab,
        'shopheas': shoptabs,
        'shopclass_list': shopclass_list,
        'goods': goods,
        'mainshows': mainshows,

    }

    cache.set('response', response_dir, 60)
    response = cache.get('response')

    return render(request, 'home/home.html', context=response_dir)


#
def market(request, childcid='0', sortid='0'):
    childcid = str(childcid)
    # 分类信息
    foodtypes = Foodtype.objects.all()

    # 商品信息
    # 默认打开　热销榜
    # 点击左侧分类　　即显示对应分类　商品信息
    # 【】
    # goods_list = Goods.objects.filter(categoryid=categoryid)

    # 客户端　需要记录　点击分类下标　【cookie　会自动携带】
    index = int(request.COOKIES.get('index', '0'))

    # 根据index 获取　对应的分类
    categoryid = foodtypes[index].typeid

    # 子分类
    if childcid == '0':
        # 根据　分类ＩＤ　获取对应分类信息
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        # 根据　分类ＩＤ　获取对应分类信息
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childcid)

        # 排序
        # 0默认综合排序   1销量排序     2价格最低   3价格最高

    if sortid == '1':
        goods_list = goods_list.order_by('-productnum')

    elif sortid == '2':
        goods_list = goods_list.order_by('price')

    elif sortid == '3':
        goods_list = goods_list.order_by('-price')

    # 获取子类信息
    childtypename = foodtypes[index].childtypenames
    # 将对应的子类拆分出来
    childtype_list = []

    for item in childtypename.split('#'):
        # item >> 全部分类：０
        # item >> 子类名称：　子类ＩＤ
        item_arr = item.split(':')
        temp_dir = {
            'name': item_arr[0],  # 子类名称
            'id': item_arr[1],  # id
        }

        childtype_list.append(temp_dir)

    response_dir = {
        #
        'foodtypes': foodtypes,
        'goods_list': goods_list,
        'childtype_list': childtype_list,
        'childcid': childcid,
    }

    # 获取登录信息
    token = request.session.get('token')
    userid = cache.get(token)

    if userid:
        user = User.objects.get(pk=userid)
        carts = user.cart_set.all()
        response_dir['carts'] = carts

    return render(request, 'macket/macket.html', context=response_dir)


#
def cart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        carts = user.cart_set.filter(number__gt=0)

        isall = True
        for cart in carts:
            if not cart.isselect:
                isall = False
        return render(request, 'cart/cart.html', context={'carts': carts, 'ilsll': isall})

    else:
        return render(request, 'cart/on-login.html')


#
def mine(request):
    token = request.session.get('token')

    user_id = cache.get(token)
    user = None
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'mine/mine.html', context={'user': user})


def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        back = request.COOKIES.get('back')


        users = User.objects.filter(email=email)
        if users.exists():
            user = users.last()
            if user.password == random_password(password):
                token = random_token()

                cache.set(token, user.id, 60 * 60 * 24)
                request.session['token'] = token

                # 根据back
                if back == 'mine':
                    return redirect('axf:mine')
                else:
                    return redirect('axf:marketbase')
            else:
                return render(request, 'mine/login.html', context={
                    'err_password': '密码错误'
                })

        else:
            return render(request, 'mine/login.html', context={'err_email': '邮箱错误'})


def logout(request):
    request.session.flush()

    return render(request, 'mine/mine.html')


def random_token():
    token = str(random.random()) + str(time.time())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()


def random_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        rank = request.POST.get('rank')

        # 储存用户
        user = User()
        user.email = email
        user.password = random_password(password)
        user.name = name
        # user.img = img
        # user.rank = rank
        user.save()

        # 状态保持
        token = random_token()

        cache.set(token, user.id, 60 * 60 * 24)

        request.session['token'] = token

        return redirect('axf:mine')


# 验证账号
def checkemail(request):
    email = request.GET.get('email')
    users = User.objects.filter(email=email)
    response_data = {}
    if users:
        response_data['status'] = 1
        return JsonResponse(response_data)
    else:
        response_data['status'] = 0
        return JsonResponse(response_data)


def addcart(request):
    token = request.session.get('token')
    print(token, '1111111111')

    # 响应数据
    response_data = {}

    # 缓存
    if token:
        userid = cache.get(token)
        print(userid, '22222222')
        if userid:
            user = User.objects.get(pk=userid)
            goodsid = request.GET.get('goodsid')
            goods = Goods.objects.get(pk=goodsid)

            # 判断商品是否存在
            # 不存在　添加新纪录
            # 存在　修改num
            carts = Cart.objects.filter(user=user).filter(goods=goods)
            if carts.exists():
                cart = carts.last()
                cart.number = cart.number + 1
                cart.save()
            else:
                cart = Cart()
                cart.user = user
                cart.number = 1
                cart.goods = goods
                cart.save()

            response_data['status'] = 1
            response_data['number'] = cart.number
            response_data['msg'] = '添加{}购物车成功{}'.format(cart.goods.productlongname, cart.number)
            return JsonResponse(response_data)

    # 未登录
    # 因为是ajax操作，所以重定向是不可以的!
    # return redirect('axf:login')

    response_data['status'] = -1
    response_data['msg'] = '请登录后操作'
    print(response_data['status'])

    return JsonResponse(response_data)


def subcart(request):
    print('fffffff')
    goodsid = request.GET.get('goodsid')
    goods = Goods.objects.get(pk=goodsid)

    # 用户
    token = request.session.get('token')
    userid = cache.get(token)
    print('userid', userid, )
    user = User.objects.get(pk=userid)

    # 获取商品购物车信息
    cart = Cart.objects.filter(user=user).filter(goods=goods).first()
    cart.number = cart.number - 1
    cart.save()

    print(goodsid)
    response_data = {
        'msg': '删减商品成功',
        'status': 1,
        'number': cart.number,

    }
    return JsonResponse(response_data)


def changecarrtselect(request):
    cartid = request.GET.get('cartid')
    print(cartid)

    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    response_data = {
        'msg': '状态修改成功',
        'status': 1,
        'isselect': cart.isselect
    }

    return JsonResponse(response_data)


def changecartall(request):
    status = request.GET.get('status')
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.all()
    if status == 'true':
        for cart in carts:
            cart.isselect = True
            cart.save()
    else:
        for cart in carts:
            cart.isselect = False
            cart.save()

    response_data = {
        'msg': '全选修改成功',
        'status': 1,
        'isselect': carts.last().isselect,
    }

    return JsonResponse(response_data)


def generate_order():
    temp = str(random.randint(100000000, 1000000000)) + str(random.randint(100000000, 1000000000))
    return temp


#生成订单
def generateorder(request):
    identifier = generate_order()
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)

    order = Order()
    order.user = user
    order.identifier = identifier
    order.save()

    carts = user.cart_set.filter(isselect=True)
    # print(goodss)
    for cart in carts:
        ordergoods = OrderGoods()
        ordergoods.order = order
        ordergoods.goods = cart.goods
        ordergoods.number = cart.number
        ordergoods.save()

        #从购物车中移除
        cart.delete()

    return render(request, 'order/orderdetail.html', context={'order': order})


def orderlist(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)

    orders = user.order_set.all()

    # status_list = ['未付款', '待发货', '待收货', '待评价', '已评价']

    return render(request, 'order/orderlist.html', context={'orders':orders})


def orderdetail(request, identifier):
    order = Order.objects.filter(identifier=identifier).first()

    return render(request, 'order/orderdetail.html', context={'order': order})


def randomtest(request):
    temp = random.randrange(2344, 7723432)
    return render(request, 'other/randomtest.html',context={'temp':temp})


def returnurl(request):
    return redirect('axf:mine')
#
#
@csrf_exempt
def appnotifyurl(request):
    if request.method == 'POST':
        # 获取到参数
        body_str = request.body.decode('utf-8')

        # 通过parse_qs函数
        post_data = parse_qs(body_str)

        # 转换为字典
        post_dic = {}
        for k, v in post_data.items():
            post_dic[k] = v[0]

        # 获取订单号
        out_trade_no = post_dic['out_trade_no']

        # 更新状态
        Order.objects.filter(identifier=out_trade_no).update(status=1)

    return JsonResponse({'msg': 'success'})


# #生成订单　返回支付地址
def pay(request):
    # print(request.GET.get('orderid'))

    orderid = request.GET.get('orderid')
    order = Order.objects.get(pk=orderid)

    sum = 0
    for orderGoods in order.ordergoods_set.all():
        sum += orderGoods.goods.price * orderGoods.number

    # 支付地址信息
    data = alipay.direct_pay(
        subject='adidas [阿迪达斯球鞋３３０３]',  # 显示标题
        out_trade_no=order.identifier,  # 爱鲜蜂 订单号
        total_amount=str(sum),  # 支付金额
        return_url='http://47.92.149.204/axf/returnurl/'
    )

    # 支付地址
    alipay_url = 'https://openapi.alipaydev.com/gateway.do?{data}'.format(data=data)

    response_data = {
        'msg': '调用支付接口',
        'alipayurl': alipay_url,
        'status': 1
    }

    return JsonResponse(response_data)


