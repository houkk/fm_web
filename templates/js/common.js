/**
 * Created by Mesogene on 3/13/16.
 */
//ajax函数定义
function restful(typeInfo, urlInfo, dataInfo) {
    /**typeInfo:操作类型；
     * urlInfo:地址；
     * dataInfo:json数据；
     * 操作类型：
     * get：获取（dataInfo为空时，查询所有；dataInfo不为空，条件查询）；
     * 查询(数据分页，暂时每页是十条数据，可后台更改)
     * post：上传；
     * put：更新(按照id)；
     * delete：删除数据（id）；
     * */

    var result = null;
    $.ajax({
        async: false,
        type: typeInfo,
        url: urlInfo,
        dataType: "json",
        //contentType:"application/json",
        data: dataInfo,
        success: function (json) {
            result = json;
        },
        error: function () {
            result = "fail";
        }
    });
    //	.success(function (json) {
    //	//result = json;
    //	result= json;
    //	return result;
    //}).error(function(json){
    //	result = json;
    //	return result;
    //});
    return result;
}

//ajax函数定义——提交数组
function restfulArray(typeInfo, urlInfo, dataInfo) {
    /**typeInfo:操作类型；
     * urlInfo:地址；
     * dataInfo:json数据；
     * 操作类型：
     * get：获取（dataInfo为空时，查询所有；dataInfo不为空，条件查询）；
     * 查询(数据分页，暂时每页是十条数据，可后台更改)
     * post：上传；
     * put：更新(按照id)；
     * delete：删除数据（id）；
     * */

    var result = null;
    $.ajax({
        async: false,
        type: typeInfo,
        url: urlInfo,
        //dataType:"json",
        contentType: "application/json",
        data: JSON.stringify(dataInfo),
        success: function (json) {
            result = json;
        },
        error: function () {
            result = "fail";
        }
    });
    //	.success(function (json) {
    //	//result = json;
    //	result= json;
    //	return result;
    //}).error(function(json){
    //	result = json;
    //	return result;
    //});
    return result;
}

/* 点击切换中间content */
function turnPage(url) {    //url:请求的url  res：存放网页的地址，使用相对地址，django会在自动搜索app的templates文件夹，子目录要自己写  url和res参数格式是 String
    $.ajax({
        type: "get",
        url: url,
        cache: false,
        dateType: "html",
        data: {area: url},
        success: function (html) {
            $('#content').empty();    //首先清空centent区
            $('#content').html(html);  //把下载的html文件添加到centent区中
        },
        error: function () {
            $('#content').empty();
            $('#content').html('<p>出了一些差错，请耐心等待修复：）</p>');
        }
    });
}


$(function(){


    $(".submenu").hide();  //默认二级菜单隐藏
    /*侧边栏鼠标点击颜色切换*/
    $('.accordion> li>a').click(function () {
        $(this).addClass('active');
        $(this).parent().siblings().find('a').removeClass('active');
        $(this).parent().siblings().find('a').removeClass('activeSec');
        $(this).siblings().toggle(500);
        $(this).parent().siblings().find('ul').hide(500);

    });

    $(".submenu> li>a").click(function () {
        $(this).addClass("activeSec");
        $(this).parent().siblings().find('a').removeClass("activeSec");
        $(this).parent().parent().siblings().addClass('active');
    });

});

//每分钟自动刷新获取实时警报
function warning(){
    var url = "/api/tbrealtimedata/?warning=realtime";
    $.get(url, function(rel) {
        var len = rel.length;
        $('.badge').html(len);
    });
}
$(function() {
    warning();
    setInterval('warning()', 1000); //注意:执行的函数需要加引号,否则会报错的
});
