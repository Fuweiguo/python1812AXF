$(function () {

    $('#content').width(innerWidth)
    /*jquery.cookie
    $.cookie(key.value.arg)

    value = $.cookie(key)

    $.cookie(key)='
    * */

    // var $index = localStorage.getItem('index')
    var index = $.cookie('index')
    var  ss = $.locals

    if (index) {
        $('.type-slider li').eq(index).addClass('active')
    } else {
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        // console.log('999999')
        // $(this).addClass('active')

        // //解决：点击后记录下标
        // localStorage.setItem('index',$(this).index())

        $.cookie('index', $(this).index(), {expires: 3, path: '/'})
    })



    //导航
    var categoryShow = false
    $('#category-bt').click(function () {
        //取反
        categoryShow = !categoryShow

        if (sortShow == categoryShow & sortShow==true){
            sortShow = !sortShow
            sortViewHide()
        }
        //三木运算
        categoryShow ? categoryViewShow() : categoryViewHide()

    })


    function categoryViewShow() {
        $('.category-view').hide()
        $('.category-view:first').show()
        $('#category-bt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
    }

    function categoryViewHide() {
        $('.category-view').hide()
        $('#category-bt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    }


    var sortShow = false
    $('#sort-bt').click(function () {
        sortShow = !sortShow
        if (sortShow == categoryShow & sortShow==true){
                categoryShow = !categoryShow
            categoryViewHide()

        }
        sortShow ? sortViewShow():sortViewHide()
    })

    function sortViewShow() {
        $('#sort-bt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
        $('.bounce-view').hide()
        $('.bounce-view:last').show()
    }


    function sortViewHide() {
        $('#sort-bt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        $('.bounce-view').hide()
    }

    $('.bounce-wrapper a').click(function () {

        $.cookie('subclass',$(this).index(),{
            expires:3 ,path:'/'
        })
        var aaa = $.cookie('subclass')
    })

    $('.bounce-view').click(function () {
        $(this).hide()
        sortShow = false
        sortViewHide()

        categoryShow=false
        categoryViewHide()

    })






//////////////////////////////////////////////
    // 影长处理
    $('.bt-wrapper>.glyphicon-minus').hide()
    $('.bt-wrapper>i').hide()

    //点击操作
    $('.bt-wrapper>.glyphicon-plus').click(function () {
        request_data = {
            'goodsid':$(this).attr('data-goodsid')
        }
        $.get('/axf/addcart/', request_data, function (response) {
            console.log(response)
            console.log('000000000000000')

            if (response.status == -1){ // 未登录
                console.log('1111111111111')
                // 设置cookie
                $.cookie('back', 'market', {expires: 3, path: '/'})

                window.open('/axf/login/', '_self')
            }
         })
    })
//
})