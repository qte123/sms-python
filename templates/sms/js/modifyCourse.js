$(function () {
    $("#submit").bind("click", function () {
        var no = $("#no").val()
        var name = $("#name").val()
        var pno = $("#pno").val()
        var credit = $("#credit").val()
        if (no !== "" && name !== "" && pno !== "" && credit !== "") {
            var flag = true
            if (!ifAge(no)) {
                alert("请输入正确的课程号")
                flag = false
            }
            if (!ifAge(pno)) {
                alert("请输入正确的先行课号")
                flag = false
            }
            if (!ifAge(credit)) {
                alert("请输入正确的学分")
                flag = false
            }
            if (flag) {
                $.ajax({
                    url: "/api/course/do/",
                    type: "POST",
                    data: {
                        action: "modify_course",
                        no: no,
                        name: name,
                        pno: pno,
                        credit: credit
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