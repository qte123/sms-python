var ifChineseName = null;
var ifAge = null;
var ifUsername = null;
var ifPassword = null;
var MAX_SIZE = 7 //最大显示行数
$(function () {
    //中文名字
    ifChineseName = function (name) {
        var reg = /[\u4e00-\u9fa5]/
        return reg.test(name);
    }

    //数字判断
    ifAge = function (number) {
        var reg = /^[0-9]*$/
        return reg.test(number);
    }

    //判断用户名是否正确格式
    ifUsername = function (username) {
        var reg = /^[a-zA-Z0-9_-]{4,16}$/;
        return reg.test(username);
    }

    //判断密码是否是正确格式
    ifPassword = function (password) {
        var reg = /^[\w]{6,12}$/;
        return reg.test(password);
    }

    $("#logout").bind("click", function () {
        $.ajax({
            url: "/api/user/logout/",
            type: "POST",
            data: {},
            dataType: "json",
            success: function (res) {
                var res1 = $(res)
                var ret = res1.attr("ret")
                var msg = res1.attr("msg")
                if (ret === 0) {
                    $(location).attr("href", "/sms/login.html")
                }
                alert(msg)
            },
            error: function () {
                console.log("出现错误！");
            }
        })
    })
})