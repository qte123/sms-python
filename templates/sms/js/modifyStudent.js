$(function () {
    $("#submit").bind("click", function () {
        var no = $("#no").val()
        var name = $("#name").val()
        var sex = $('input:radio:checked').val()
        var age = $("#age").val()
        var department = $("#department").val()
        if (no !== "" && name !== "" && sex !== "" && age !== "" && department !== "") {
            var flag = true
            if (!ifAge(no)) {
                alert("请输入正确的学号")
                flag = false
            }
            if (!ifChineseName(name)) {
                alert("请输入正确的姓名")
                flag = false
            }
            if (!ifAge(age)) {
                alert("请输入正确的年龄")
                flag = false
            }
            if (flag) {
                $.ajax({
                    url: "/api/student/do/",
                    type: "POST",
                    data: {
                        action: "modify_student",
                        no: no,
                        name: name,
                        sex: sex,
                        age: age,
                        department: department
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