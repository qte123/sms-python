$(function () {
    var name = ""
    var pageIndex = 0
    var len = 0
    $("#select").bind("click", function () {
        var select_value = $("#select_value")
        name = select_value.val()
        select_value.val("")
        pageIndex = 0
        fn(name, pageIndex)
    })
    $("#all_btn").bind("click", function () {
        name = ""
        pageIndex = 0
        fn(name, pageIndex)
    })
    $("#prev").bind("click", function () {
        if (pageIndex > 0) {
            pageIndex--
        } else {
            alert("前面没有了")
        }
        fn(name, pageIndex)
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
        fn(name, pageIndex)
    })
    fn = function (name, pageIndex1) {
        $.ajax({
            url: "/api/course/do/",
            type: "POST",
            data: {
                action: "list_course",
                name: name,
                pageIndex: pageIndex1
            },
            dataType: "json",
            success: function (res) {
                var res1 = $(res)
                var courseList = res1.attr("retlist")
                len = courseList.length
                $("table tr:not(:first)").remove();
                $(courseList).each(function (i, course) {
                    var courseObj = $(course);
                    var no = courseObj.attr("no")
                    var name = courseObj.attr("name")
                    var pno = courseObj.attr("pno")
                    var credit = courseObj.attr("credit")
                    $('table').append(' <tr>\n' +
                        '                    <td>' + no + '</td>\n' +
                        '                    <td>' + name + '</td>\n' +
                        '                    <td>' + pno + '</td>\n' +
                        '                    <td>' + credit + '</td>\n' +
                        '                </tr>')
                })
            },
            error: function () {
                console.log("出现错误！");
            }
        })
    }
    fn(name, pageIndex)
})