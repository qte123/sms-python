$(function () {
    $("#sub").bind("click", function () {
        var username = $("#username").val()
        var password = $("#password").val()
        $.ajax({
            url: "/api/user/login/",
            type: "POST",
            data: {
                username: username,
                password: password
            },
            dataType: "json",
            success: function (res) {
                var res1 = $(res)
                var ret = res1.attr("ret")
                var msg = res1.attr("msg")
                var type = res1.attr("type")
                if (ret === 0) {
                    if (type === 0) $(location).attr("href", "/sms/html/root/grade.html")
                    else $(location).attr("href", "/sms/html/root/index.html")
                }
                alert(msg)
            },
            error: function () {
                console.log("出现错误！");
            }
        })
    })
})