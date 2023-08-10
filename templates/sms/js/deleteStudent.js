$(function () {
    $("#submit").bind("click", function () {
        var no = $("#no").val()
        if (no !== "") {
            var flag = true
            if (!ifAge(no)) {
                alert("请输入正确的学号")
                flag = false
            }
            if (flag) {
                $.ajax({
                    url: "/api/student/do/",
                    type: "POST",
                    data: {
                        action: "delete_student",
                        no: no,
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