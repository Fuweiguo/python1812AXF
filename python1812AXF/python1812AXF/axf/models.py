from django.db import models

# 基础类
class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True



class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'



class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'


class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'


class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


# 主页显示
class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models. CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)


# 商品　分类
class Foodtype(models.Model):

    typeid = models.CharField(max_length=10)

    typename = models.CharField(max_length=100)

    childtypenames = models.CharField(max_length=200)

    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'



#商品模型　类
class Goods(models.Model):

    productid = models.CharField(max_length=10)

    productimg = models.CharField(max_length=100)

    productname = models.CharField(max_length=100)

    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=0)

    pmdesc = models.IntegerField(default=0)

    specifics = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    marketprice = models.DecimalField(max_digits=8, decimal_places=2)
    #
    categoryid = models.IntegerField()
    #
    childcid = models.IntegerField()
    #
    childcidname = models.CharField(max_length=100)
    #
    dealerid = models.CharField(max_length=100)
    #
    storenums = models.IntegerField()
    #
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

# 用户模型类
class User(models.Model):
    #
    email = models.CharField(max_length=40,unique=True)
    #
    password = models.CharField(max_length=256)
    #
    name = models.CharField(max_length=100)
    #　
    img = models.CharField(max_length=40,default='axf.png')
    #
    rank = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_user'

#　购物车模型　类
class Cart(models.Model):

    user = models.ForeignKey(User)


    goods = models.ForeignKey(Goods)

    #
    number = models.IntegerField()


    isselect = models.BooleanField(default=True)

    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_cart'



# 订单 模型类
# 一个用户 对应 多个订单
class Order(models.Model):
    # 用户
    user = models.ForeignKey(User)
    # 创建时间
    createtime = models.DateTimeField(auto_now_add=True)
    # 更新时间
    updatetime = models.DateTimeField(auto_now=True)
    # 状态
    # -1 过期
    # 0 未付款
    # 1 已付款，待发货
    # 2 已发货，待收货
    # 3 已收货，待评价
    # 4 已评价
    status = models.IntegerField(default=0)
    # 订单号
    identifier = models.CharField(max_length=256)

    class Meta:
        db_table = 'axf_order'



# 订单商品 模型类
# 一个订单 对应 多个商品(订单商品)
class OrderGoods(models.Model):
    # 订单
    order = models.ForeignKey(Order)
    # 商品
    goods = models.ForeignKey(Goods)

    ## 商品选择规格
    number = models.IntegerField()

    class Meta:
        db_table = 'axf_ordergoods'