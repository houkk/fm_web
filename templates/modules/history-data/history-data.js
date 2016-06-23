/**
 * Created by Mesogene on 3/13/16.
 */

(function (){
    "use strict";

    //readstatus=0，未超过阀值；
    //readstatus=1，超过阀值未读；
    //readstatus=2，超过阀值已读；

   /* var json = {"fkey_areaid":6,"fkey_fieldid":1,"collecttime":"2016-03-15 12:30:00","readstatus":1,'temperdata':40,'humiditydata':50,"phdata":8};

    $('#submit').click(function () {
        var result = restful("post","/api/tbrealtimedata/",json);
    if(result != "fail"){
        console.log(result);
    }

    });*/

    //温度、ph、湿度阀值设定
    var limit = restful('get','/api/tbwarnlimit/');
    var tempermin = parseFloat(limit[0].min_temperlimit);
    var tempermax = parseFloat(limit[0].max_temperlimit);
    var phmin = parseFloat(limit[0].min_ph);
    var phmax = parseFloat(limit[0].max_ph);
    var humiditymin = parseFloat(limit[0].min_water);
    var humiditymax = parseFloat(limit[0].max_water);

    var $table = $("#history-data").bootstrapTable({
        columns: [ {
            field: "fkey_fieldid",
            title: "田地",
            align: "center",
            visible: true
        }, {
            field: "fkey_areaid",
            align: "center",
            title: "块",
            sortable: true
        }, {
            field: "temperdata",
            title: "温度",
            align: "center",
            formatter:function(value,row,index){
                return value + " ℃";
            }
        }, {
            field: "humiditydata",
            title: "湿度",
            align: "center",
            formatter:function(value,row,index){
                return value  + " %";
            }
        }, {
            field: "phdata",
            title: "PH值",
            align: "center"
        }, {
            field: "collecttime",
            title: "采集时间",
            align: "center"
            /*formatter:function(value,row,index){
                return value;
            }*/
        }],
        classes:"table table-no-bordered",
        pagination: "true",
        pageSize: 10,
        pageList: "[10, 30, 50]",
        locale: "zh-CN",
        smartDisplay: true,
        url: "/api/tbrealtimedata/?warning=history"
    });



    //按钮刷新功能
    $('#refresh').click(function () {
        $table.bootstrapTable('refresh', {
            url: "/api/tbrealtimedata/?warning=history"
        });
    });

})();