






















$(function () {
    /*jquery.cookie
    $.cookie(key.value.arg)

    value = $.cookie(key)

    $.cookie(key)='
    * */



    // var $index = localStorage.getItem('index')
    var index = $.cookie('index')

    console.log(index)
    if (index){
        $('.type-slider li').eq(index).addClass('active')
    }else {
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        // console.log(1)
        // $(this).addClass('active')

        // //解决：点击后记录下标
        // localStorage.setItem('index',$(this).index())

        $.cookie('index',$(this).index(),{expires:3,path:'/'})
    })
})