$(function () {

    //　邮箱验证
    $('#email_v input').blur(function () {
        //输入是否正确
        var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式

        //空　不需要验证处理
        if ($(this).val() == ''){
            $('#email_v').removeClass('has-error','has-success')
            $('#email_v .glyphicon').removeClass('glyphicon-remove','glyphicon-ok')
            console.log('空')
            return
        }

        //格式是否正确
        if (reg.test($(this).val())) {　//符合

            console.log('格式正确')
            reqest_data = {
                'email': $(this).val()
            }
            //账号是否可用
            $.get('/axf/checkemail/', reqest_data, function (response) {
                if (response.status){
                    $('#example').attr('data-content','账号可用')
                    $('#email_v').removeClass('has-error').addClass('has-success')
                $('#email_v>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                }else {
                    $('#example').attr('data-content','账号不可用')
                    $('#email_v').removeClass('has-error').addClass('has-success')
                    $('#email_v>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                }
            })
        } else { //不符合
            $('#example').attr('data-content','数据格式不正确')
            $('#email_v').removeClass('has-success').addClass('has-error')
            $('#email_v .glyphicon').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            console.log('格式不正确')
        }
    })



    $('#password_v input').blur(function () {
        var reg = new RegExp("^[a-zA-Z0-9_]{6,10}$");
        if(($(this).val() == '')){
            $('#password_v').removeClass('has-error','has-success')
            $('#password_v .glyphicon').removeClass('glyphicon-remove','glyphicon-ok')
            console.log('空')
            return
        }

        if (reg.test($(this).val())){
            $('#password_v').removeClass('has-error').addClass('has-success')
            $('#password_v .glyphicon').removeClass('glyphicon-remove').addClass('glyphicon-ok')

            console.log('密码格式正确')
        }else {
            $('#password_v').removeClass('has-success').addClass('has-error')
            $('#password_v .glyphicon').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            console.log('密码格式错误')
        }
    })


    $('#name_v input').blur(function () {
        if ($(this).val() == ''){
            $('#name_v').removeClass('has-error','has-success')
            $('#name_v .glyphicon').removeClass('glyphicon-remove','glyphicon-ok')
            console.log('空')
            return
        }


        if ($(this).val().length>=3 && $(this).val().length<=6 ){
            $('#name_v').removeClass('has-error').addClass('has-success')
            $('#name_v .glyphicon').removeClass('glyphicon-remove').addClass('glyphicon-ok')

            console.log('昵称式正确')
        }else {
            $('#name_v').removeClass('has-success').addClass('has-error')
            $('#name_v .glyphicon').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            console.log('昵称格式错误')
        }
    })

    $('#register_button').click(function () {
        var isregister = true
        $('.register .input-group').each(function () {
            if(!$(this).is('.has-success')){
                isregister = false
            }
        })
        if (isregister){
            $('.register form').submit()
        }
    })
})