$(function () {
    $("#submit").bind("click", function () {
        var student_no = $("#student_no").val()
        var course_name = $("#course_name").val()
        var label = $("#label")
        if (student_no !== '' && course_name !== '') {
            $.ajax({
                url: "/api/sc/select/",
                type: "POST",
                data: {
                    action: "grade_select",
                    student_no: student_no,
                    course_name: course_name
                },
                dataType: "json",
                success: function (res) {
                    var res1 = $(res)
                    var ret = res1.attr("ret")
                    var msg = res1.attr("msg")
                    if (ret === 0) {
                        var grade = res1.attr("grade")
                        label.html(grade)
                    }
                    alert(msg)
                },
                error: function () {
                    console.log("出现错误！");
                }
            })
        } else {
            alert("输入不能为空")
        }
    })
})