$(function () {
    $("#submit").bind("click", function () {
        var username = $("#username").val()
        var status = $('input:radio:checked').val()
        if (username !== "" && status !== "") {
            var flag = true
            if (!ifUsername(username)) {
                alert("请输入正确的用户名")
                flag = false
            }
            if (flag) {
                $.ajax({
                    url: "/api/user/do/",
                    type: "POST",
                    data: {
                        action: "modify_status",
                        username: username,
                        status: status
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