$(function () {
    var student_no = ""
    var pageIndex = 0
    var len = 0
    $("#select").bind("click", function () {
        var select_value = $("#select_value")
        student_no = select_value.val()
        select_value.val("")
        pageIndex = 0
        fn(student_no, pageIndex)
    })
    $("#all_btn").bind("click", function () {
        student_no = ""
        pageIndex = 0
        fn(student_no, pageIndex)
    })
    $("#prev").bind("click", function () {
        if (pageIndex > 0) {
            pageIndex--
        } else {
            alert("前面没有了")
        }
        fn(student_no, pageIndex)
    })

    $("#next").bind("click", function () {
        if (len % MAX_SIZE !== 0) {
            len = parseInt("" + len / MAX_SIZE)
        } else {
            len = parseInt("" + (len / MAX_SIZE - 1))
        }
        if (pageIndex < len) {
            pageIndex++
        } else {
            alert("后面没有了")
        }
        fn(student_no, pageIndex)
    })
    fn = function (student_no, pageIndex1) {
        $.ajax({
            url: "/api/sc/do/",
            type: "POST",
            data: {
                action: "list_sc",
                student_no: student_no,
                pageIndex: pageIndex1
            },
            dataType: "json",
            success: function (res) {
                var res1 = $(res)
                var scList = res1.attr("retlist")
                len = scList.length
                $("table tr:not(:first)").remove();
                $(scList).each(function (i, sc) {
                    var scObj = $(sc);
                    var student_no = scObj.attr("student_no")
                    var student_name = scObj.attr("student_name")
                    var course_name = scObj.attr("course_name")
                    var grade = scObj.attr("grade")
                    $('table').append(' <tr>\n' +
                        '                    <td>' + student_no + '</td>\n' +
                        '                    <td>' + student_name + '</td>\n' +
                        '                    <td>' + course_name + '</td>\n' +
                        '                    <td>' + grade + '</td>\n' +
                        '                </tr>')
                })
            },
            error: function () {
                console.log("出现错误！");
            }
        })
    }
    fn(student_no, pageIndex)
})