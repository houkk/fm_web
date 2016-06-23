/**
 * Created by Mesogene on 3/13/16.
 */

$("#crops-info").bootstrapTable({
    columns:[{
        field:"cropsinfoid",
        title:"农作物编号",
        visible:false
    },{
        field:"cropsname",
        title:"农作物名称",
        sortable:true
    },{
        field:"cropslife",
        title:"生命周期",
        sortable:true
    },{
        field:"cropsdesc",
        title:"描述",
        sortable:true
    },{
        field:"operate",
        title:"详情",
        events: {
            "click .detail": function (e, value, row, index) {
                var msg=restful("get","/api/tbcropsinfo/"+row.cropsinfoid,null);
                var showingField="<div class='row'>" +
                    "<div class='col-md-12'><div class='panel panel-success'>" +
                    "<div class='panel-heading'><h4 class='panel-title'>农作物介绍</h4></div>"+
                    "<div class='panel-body'>" +
                    "<div class='col-md-12'>农作物名称："+msg.cropsname+"</div>" +
                    "<div class='col-md-12'>农作物描述："+msg.cropsdesc+"</div>" +
                    "<div class='col-md-12'>生命周期："+msg.cropslife+"</div>" +
                    "<div class='col-md-12'>农作物图片：<br/><img style='width: 200px;height: 200px' src='"+msg.cropspic+"'/></div>" +
                    "</div>" +
                    "</div></div>" +
                    "</div>";

                $("#crops-showing").html(showingField);

            }
        },
        formatter: function operateFormatter(){
            return '<a class="detail" title="查看详情"><i class="glyphicon glyphicon-eye-open"></i>'
        }
    }],
    pagination:"true",
    pageSize:10,
    pageList:"[10, 30, 50]",
    locale:"zh-CN",
    smartDisplay:true,
    url:"/api/tbcropsinfo/"
});