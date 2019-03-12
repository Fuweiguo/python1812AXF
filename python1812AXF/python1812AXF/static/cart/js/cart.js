$(function () {
    $('.cart').width(innerWidth)
    isall_v()
    total()

    //选中处理
    $('.cart .confirm-wrapper').click(function () {

        var $span = $(this).find('span')

        reqest_data = {
            'cartid': $(this).attr('data-cardid')

        }

        $.get('/axf/changecarrtselect/', reqest_data, function (response) {
            console.log(response)
            if (response.status == 1) {
                if (response.isselect) {
                    $span.removeClass('no').addClass(' glyphicon glyphicon-ok')
                } else {
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }
            }
            isall_v()
            total()
        })
    })

    //全选/取消全选
    $('.cart .all').click(function () {
        console.log('点击')
        var isall = $(this).attr('isall')
        var $span = $(this).find('span')
        console.log(isall, 'isall')
        //修改　全选　按钮状态
        isall = (isall == 'false') ? true : false

        $(this).attr('isall', isall)
        if (isall) {
            $span.removeClass('no').addClass(' glyphicon glyphicon-ok')
        } else {
            $span.removeClass('glyphicon glyphicon-ok').addClass('no')
        }

        reqest_data = {
            'status': isall
        }
        $.get('/axf/changecartall/', reqest_data, function (response) {
            console.log(response)

            if (response.status == 1) {
                $('.confirm-wrapper').each(function () {
                    if (isall) {
                        $(this).find('span').removeClass('no').addClass(' glyphicon glyphicon-ok')
                    } else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                    // total()
                })
                // total()
            }
            total()
        })
        //  问题　在ajax外调用　有结算迟钝问题
        // total()
    })


    function isall_v() {
        var num = 0
        var nums = $('.confirm-wrapper').length
        $('.confirm-wrapper').each(function () {
            if ('no' == $(this).find('span').attr('class')) {
                num += 1
                console.log('ture')
            }
        })

        if (num == 0) {
            $('.all').attr('isall', true)
            $('.all').find('span').removeClass('no').addClass(' glyphicon glyphicon-ok')
        } else {
            $('.all').attr('isall', false)
            $('.all').find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
        }
        console.log(num, 'num')
    }

    function total() {
        var total_num = 0

        console.log($('.detail .num'), '++++++++')
        $('.cart li').each(function () {

            var $isselect = $(this).find('.glyphicon')
            if ($isselect.length) {
                number = $(this).find('.num').attr('data-number')
                price = $(this).find('.price').attr('data-price')
                total_num += price * number
            }
        })
        $('.total>b').html(total_num)
        console.log(total_num, 'iiiiiiii')
        total_num = 0
    }
})