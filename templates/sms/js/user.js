$(function () {
    var username = ""
    var pageIndex = 0
    var usertype = ""
    var len = 0

    function formatDate(time) {
        var date = new Date(time);

        var year = date.getFullYear(),
            month = date.getMonth() + 1,//月份是从0开始的
            day = date.getDate(),
            hour = date.getHours(),
            min = date.getMinutes(),
            sec = date.getSeconds();
        var newTime = year + '-' +
            month + '-' +
            day + ' ' +
            hour + ':' +
            min + ':' +
            sec;
        return newTime;
    }

    $("#select").bind("click", function () {
        var select_value = $("#select_value")
        username = select_value.val()
        select_value.val("")
        pageIndex = 0
        usertype = ""
        fn(username, usertype, pageIndex)
    })
    $("#all_btn").bind("click", function () {
        usertype = ""
        pageIndex = 0
        username = ""
        fn(username, usertype, pageIndex)
    })
    $("#teacher_btn").bind("click", function () {
        usertype = 1
        pageIndex = 0
        fn(username, usertype, pageIndex)
    })
    $("#student_btn").bind("click", function () {
        usertype = 0
        pageIndex = 0
        fn(username, usertype, pageIndex)
    })
    $("#prev").bind("click", function () {
        if (pageIndex > 0) {
            pageIndex--
        } else {
            alert("前面没有了")
        }
        fn(username, usertype, pageIndex)
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
        fn(username, usertype, pageIndex)
    })
    fn = function (username, usertype, pageIndex1) {
        $.ajax({
            url: "/api/user/do/",
            type: "POST",
            data: {
                action: "list_user",
                username: username,
                usertype: usertype,
                pageIndex: pageIndex1
            },
            dataType: "json",
            success: function (res) {
                var res1 = $(res)
                var userList = res1.attr("retlist")
                len = userList.length
                $("table tr:not(:first)").remove();
                $(userList).each(function (i, user) {
                    var userObj = $(user);
                    var username = userObj.attr("username")
                    var password = userObj.attr("password")
                    var is_activate = userObj.attr("is_activate")
                    var status = ""
                    if (is_activate === Number(0)) {
                        status = "停用"
                    } else {
                        status = "启用"
                    }
                    var last_login = userObj.attr("last_login")
                    $('table').append(' <tr>\n' +
                        '                    <td>' + username + '</td>\n' +
                        '                    <td>' + password + '</td>\n' +
                        '                    <td>' + status + '</td>\n' +
                        '                    <td>' + formatDate(last_login) + '</td>\n' +
                        '                </tr>')
                })
            },
            error: function () {
                console.log("出现错误！");
            }
        })
    }
    fn(username, usertype, pageIndex)
})

