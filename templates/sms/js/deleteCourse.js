$(function () {
    $("#submit").bind("click", function () {
        var name = $("#name").val()
        if (name !== "") {
            var flag = true
            if (flag) {
                $.ajax({
                    url: "/api/course/do/",
                    type: "POST",
                    data: {
                        action: "delete_course",
                        name: name
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