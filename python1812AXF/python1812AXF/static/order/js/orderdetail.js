$(function () {
    $('#alipay').click(function () {
        request_data = {
            'orderid':$(this).attr('data-orderid')
        }
        console.log('我不卡')
        $.get('/axf/pay/',request_data,function (response) {
            console.log('++++++++')
            if (response.status == 1){
                window.open(response.alipayurl, target='_self')
            }
        })
    })
})