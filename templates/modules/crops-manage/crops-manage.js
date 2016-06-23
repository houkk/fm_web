/**
 * Created by Mesogene on 3/13/16.
 */


var areaName=restful("get","/api/tbarea/",null);
var area="";
$.each(areaName, function (i,n) {
    area+="<option value="+areaName[i].areaid+">"+areaName[i].areaname+"</option>";
});
$("#area-name").html(area);



var cropsName=restful("get","/api/tbcropsinfo/",null);
var crops="";
$.each(cropsName, function (i, n) {
    crops+="<option value="+cropsName[i].cropsinfoid+">"+cropsName[i].cropsname+"</option>";
});
$("#crops-name").html(crops);


$("#create").click(function(){

});

$("#crops-manage").bootstrapTable({
    columns:[{
        field:"fertilizerinfoid",
        title:"编号",
        visible:false
    },{
        field:"fertilizerinfoid",
        title:"区域名称",
        sortable:true
    },{
        field:"fertilizerinfoid",
        title:"农作物名称",
        sortable:true
    },{
        field:"fertilizerinfoid",
        title:"种植时间",
        sortable:true
    },{
        field:"fertilizerinfoid",
        title:"建议收获时间",
        sortable:true
    },{
        field:"fertilizerinfoid",
        title:"预估产量",
        sortable:true
    },]
});

