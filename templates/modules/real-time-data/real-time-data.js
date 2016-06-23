/**
 * Created by Mesogene on 3/13/16.
 */
(function () {
    "use strict";
    var total_area = restful('get','/api/tbarea/');
    var total_field = restful('get', '/api/tbfield/');

    if (total_area != "fail") {
        //初始化两个select
        $('#area_first').html(total_area[0].areaname);
        for(var i in total_area){
            var str2 = '<li><a name="selecta" class='+i+'>'+total_area[i].areaname+'</a></li>';
            $('#area ul').append(str2);
        }

        $('#field ul').html('');
        var area_field = restful('get', '/api/tbfield/?fkey_areaid=' + total_area[0].areaid);
        if (jQuery.isEmptyObject(area_field) || area_field == 'fail') {
            //alert('田块为空或者数据获取失败！')
        }
        else{
            $('#field_first').html(area_field[0].fieldname);
            for (var j in area_field) {
                var str = '<li><a name="selectf" class=' + j + '>' + area_field[j].fieldname + '</a></li>';
                $('#field ul').append(str);
            }
        }
    }


    $('a[name="selecta"]').click(function () {
        var id = $(this).attr('class');
        $('#area_first').html(total_area[id].areaname);

        $('#field ul').html('');
        var area_field = restful('get', '/api/tbfield/?fkey_areaid=' + total_area[id].areaid);
        if (jQuery.isEmptyObject(area_field) || area_field == 'fail') {
            alert('田块为空或者数据获取失败！')
        }
        else{
            $('#field_first').html(area_field[0].fieldname);
            for (var j in area_field) {
                var str = '<li><a name="selectf" class=' + j + '>' + area_field[j].fieldname + '</a></li>';
                $('#field ul').append(str);
            }
        }

    });
    $('a[name="selectf"]').click(function () {
        var id = $(this).attr('class');
        $('#field_first').html(total_field[id].fieldname);

    });

    temper();

})();


function temper() {

    var dom = document.getElementById("chart_temper");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;

    var msg = null;
    var time = [];
    var temp = [];

    function getdata(){
        msg = restful('get','/api/tbrealtimedata/');
        time = [];
        temp = [];
        for(var i in msg){
            time.push(msg[i].collecttime);
            temp.push(msg[i].temperdata);
        }
    }
    getdata();
            console.log(temp);

    //setInterval('getdata()', 1000);

    option = {
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: time
        },
        yAxis: {
            /*boundaryGap: [-20, 200],
            type: 'value'*/
        },
        series: [
            {
                name: '成交',
                type: 'line',
                smooth: true,
                symbol: 'none',
                stack: 'a',
                areaStyle: {
                    normal: {}
                },
                data: temp
            }
        ]
    };

    app.timeTicket = setInterval(function () {
        getdata();
        myChart.setOption({
            xAxis: {
                data: time
            },
            series: [{
                name: '成交',
                data: temp
            }]
        });
    }, 500);
    ;
    if (option && typeof option === "object") {
        var startTime = +new Date();
        myChart.setOption(option, true);
        var endTime = +new Date();
        var updateTime = endTime - startTime;
        console.log("Time used:", updateTime);
    }

}

