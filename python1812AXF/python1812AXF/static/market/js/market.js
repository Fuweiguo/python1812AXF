$(function () {

    $('#content').width(innerWidth)
    /*jquery.cookie
    $.cookie(key.value.arg)

    value = $.cookie(key)

    $.cookie(key)='
    * */

    // var $index = localStorage.getItem('index')
    var index = $.cookie('index')

    console.log(index)
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


    var categoryShow = false
    $('#category-bt').click(function () {
        //取反
        categoryShow = !categoryShow
        console.log('左',categoryShow)

        if (sortShow == categoryShow & sortShow==true){
            sortShow = !sortShow
            console.log('左',categoryShow,'右',sortShow)
            sortViewHide()
        }
        //三木运算
        categoryShow ? categoryViewShow() : categoryViewHide()

    })


    function categoryViewShow() {
        console.log('左' ,categoryShow)
        $('.category-view').show()
        $('#category-bt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
    }

    function categoryViewHide() {
        console.log('hide',categoryShow)
        $('.category-view').hide()
        $('#category-bt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
    }

    var sortShow = false
    $('#sort-bt').click(function () {
        sortShow = !sortShow
        console.log('右',sortShow)

        if (sortShow == categoryShow & sortShow==true){
                categoryShow = !categoryShow
            console.log('左',categoryShow,'右',sortShow,'pppppp')
            categoryViewHide()

        }
        sortShow ? sortViewShow():sortViewHide()
    })

    function sortViewShow() {
        console.log('左',categoryShow,'右',sortShow,'pppppp')
        $('#sort-bt i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down')
        $('.bounce-view').show()
    }


    function sortViewHide() {
        console.log('hide',sortShow)
        $('#sort-bt i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up')
        $('.bounce-view').hide()
    }

    $('.bounce-wrapper a').click(function () {

        $.cookie('subclass',$(this).index(),{
            expires:3 ,path:'/'
        })
        var aaa = $.cookie('subclass')
        console.log(aaa,'llllllll')
    })

    $('.bounce-view').click(function () {
        console.log('蒙层')
        $(this).hide()
        sortShow = false
        sortViewHide()

        categoryShow=false
        categoryViewHide()

    })

})