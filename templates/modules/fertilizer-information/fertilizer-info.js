/**
 * Created by Mesogene on 3/13/16.
 */

$("#fertilizer-info").bootstrapTable({
    columns:[{
        field:"fertilizerinfoid",
        title:"肥料编号",
        visible:false
    },{
        field:"fertilizername",
        title:"肥料名称",
        sortable:true
    },{
        field:"fertilizerdesc",
        title:"描述",
        sortable:true
    },{
        field:"usedesc",
        title:"使用描述",
        sortable:true
    },{
        field:"operate",
        title:"详情",
        events: {
            "click .detail": function (e, value, row, index) {
                var msg=restful("get","/api/tbfertilizerinfo/"+row.fertilizerinfoid,null);
                var showingField="<div class='row'>" +
                    "<div class='col-md-12'><div class='panel panel-success'>" +
                    "<div class='panel-heading'><h4 class='panel-title'>肥料介绍</h4></div>"+
                    "<div class='panel-body'>" +
                    "<div class='col-md-12'>肥料名称："+msg.fertilizername+"</div>" +
                    "<div class='col-md-12'>描述："+msg.fertilizerdesc+"</div>" +
                    "<div class='col-md-12'>使用描述："+msg.usedesc+"</div>" +
                    "<div class='col-md-12'>肥料图片：<br/><img style='width: 200px;height: 200px' src='"+msg.fertilizerpic+"'/></div>" +
                    "</div>" +
                    "</div></div>" +
                    "</div>";

                $("#fertilizer-showing").html(showingField);

            }
        },
        formatter: function operateFormatter(){
            return '<a class="detail" title="查看详情"><i class="glyphicon glyphicon-eye-open"></i>'
        }
    }],
    pageSize:10,
    pageList:"[10,30.50]",
    locale:"zh-CN",
    smartDisplay:true,
    url:baseAddress+"/api/tbfertilizerinfo/"
});