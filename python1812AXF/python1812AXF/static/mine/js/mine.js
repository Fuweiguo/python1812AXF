$(function () {
    $('#content').width(innerWidth)

     $('#login-i').click(function () {
        // 设置cookie
        $.cookie('back', 'mine', {expires: 3, path: '/'})

        window.open('/axf/login/', '_self')
    })
})