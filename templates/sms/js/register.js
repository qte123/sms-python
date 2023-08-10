$(function () {
    $("#submit").bind("click", function () {
        var username = $("#username").val()
        var password = $("#password").val()
        var password2 = $("#password2").val()
        var type = $('input:radio:checked').val()
        if (username !== "" && password !== "" && password2 !== "") {
            var flag = true
            if (!ifUsername(username)) {
                alert("账号格式不对")
                flag = false
            }
            if (!ifPassword(password)) {
                alert("密码格式不对")
                flag = false
            }
            if (password !== password2) {
                alert("两次密码不一致")
                flag = false
            }
            if (flag) {
                $.ajax({
                    url: "/api/user/register/",
                    type: "POST",
                    data: {
                        username: username,
                        password: password,
                        type: type

                    },
                    dataType: "json",
                    success: function (res) {
                        var res1 = $(res)
                        var ret = res1.attr("ret")
                        var msg = res1.attr("msg")
                        alert(msg)
                    },
                    error: function () {
                        console.log("出现错误！");
                    }
                })
            }
        } else {
            alert("输入不能为空")
        }
    })
})