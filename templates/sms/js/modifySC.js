$(function () {
    $("#submit").bind("click", function () {
        var student_no = $("#student_no").val()
        var course_name = $("#course_name").val()
        var grade = $("#grade").val()
        if (student_no !== "" && course_name !== "" && grade !== "") {
            var flag = true
            if (!ifAge(student_no)) {
                alert("请输入正确的学号")
                flag = false
            }
            if (!ifAge(grade)) {
                alert("请输入正确的成绩")
                flag = false
            }
            if (flag) {
                $.ajax({
                    url: "/api/sc/do/",
                    type: "POST",
                    data: {
                        action: "modify_sc",
                        student_no: student_no,
                        course_name: course_name,
                        grade: grade
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