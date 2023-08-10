$(function () {
    var no = ""
    var pageIndex = 0
    var len = 0

    $("#select").bind("click", function () {
        var select_value = $("#select_value")
        no = select_value.val()
        select_value.val("")
        pageIndex = 0
        fn(no, pageIndex)
    })
    $("#all_btn").bind("click", function () {
        no = ""
        pageIndex = 0
        fn(no, pageIndex)
    })
    $("#prev").bind("click", function () {
        if (pageIndex > 0) {
            pageIndex--
        } else {
            alert("前面没有了")
        }
        fn(no, pageIndex)
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
        fn(no, pageIndex)
    })
    fn = function (no, pageIndex1) {
        $.ajax({
            url: "/api/student/do/",
            type: "POST",
            data: {
                action: "list_student",
                no: no,
                pageIndex: pageIndex1
            },
            dataType: "json",
            success: function (res) {
                var res1 = $(res)
                var studentList = res1.attr("retlist")
                len = studentList.length
                $("table tr:not(:first)").remove();
                $(studentList).each(function (i, student) {
                    var studentObj = $(student);
                    var no = studentObj.attr("no")
                    var name = studentObj.attr("name")
                    var sex = studentObj.attr("sex")
                    var age = studentObj.attr("age")
                    var department = studentObj.attr("department")
                    $('table').append(' <tr>\n' +
                        '                    <td>' + no + '</td>\n' +
                        '                    <td>' + name + '</td>\n' +
                        '                    <td>' + sex + '</td>\n' +
                        '                    <td>' + age + '</td>\n' +
                        '                    <td>' + department + '</td>\n' +
                        '                </tr>')
                })
            },
            error: function () {
                console.log("出现错误！");
            }
        })
    }
    fn(no, pageIndex)
})