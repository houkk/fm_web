/**
 * Created by Mesogene on 3/13/16.
 */

$("#pesticide-info").bootstrapTable({
    columns:[{
        field:"pesticidesinfoid",
        title:"农药编号",
        visible:false
    },{
        field:"pesticidesname",
        title:"农药名称",
        sortable:true
    },{
        field:"pesticidesdesc",
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
                var msg=restful("get","/api/tbpesticidesinfo/"+row.pesticidesinfoid,null);
                var showingField="<div class='row'>" +
                    "<div class='col-md-12'><div class='panel panel-success'>" +
                    "<div class='panel-heading'><h4 class='panel-title'>农药介绍</h4></div>"+
                    "<div class='panel-body'>" +
                    "<div class='col-md-12'>农药名称："+msg.pesticidesname+"</div>" +
                    "<div class='col-md-12'>描述："+msg.pesticidesdesc+"</div>" +
                    "<div class='col-md-12'>使用描述："+msg.usedesc+"</div>" +
                    "<div class='col-md-12'>农药图片：<br/><img style='width: 200px;height: 200px' src='"+msg.pesticidespic+"'/></div>" +
                    "</div>" +
                    "</div></div>" +
                    "</div>";

                $("#pesticides-showing").html(showingField);

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
    url:baseAddress+"/api/tbpesticidesinfo/"
});