$(document).ready(function() {
    var lastSel;
    var editoptions_types = (function () {
        var list = null;

        $.ajax({
            'async': false,
            'global': false,
            'url': '_get_types',
            'dataType': 'json',
            'success': function (data) {
                list = data.types;
            }
        });

        return list;
    })();
    
    //Construct a jqGrid object
    $("#entries").jqGrid({
       	url:'/_get_entries',
    	datatype: "json",
       	colNames:['name', 'type', 'library','from_buss','to_buss', 'length', 'ampacity'],
       	colModel:[
       		{name:'name',index:'name', width:90, sortable:true, editable: true, editoptions:{size:"20",maxlength:"50"}},
       		{name:'type',index:'type', width:80, align:"right", editable: true, edittype:"select", 
       		    editoptions: {value: editoptions_types}},
       		{name:'library',index:'library', width:80, editable: true, editoptions:{size:"20",maxlength:"50"}, align:"center"},		
       		{name:'from_buss',index:'from_buss', width:80, editable: true, editoptions:{size:"20",maxlength:"50"}, align:"center"},		
       		{name:'to_buss',index:'to_buss', width:80, sortable:false, editable: true, editoptions:{size:"20",maxlength:"50"}, align:"center"},
       		{name:'length',index:'length', width:80, editable: true, editoptions:{size:"20",maxlength:"50"}, align:"center"},		
       		{name:'ampacity',index:'ampacity', width:80, editable: true, editoptions:{size:"20",maxlength:"50"}, sortable:false,align:"center"}
       	],
       	rowNum:10,
       	rowList:[5,10,20],
       	pager: '#pager',
       	sortname: 'id',
        viewrecords: true,
        width: '905',
        sortorder: "desc",
        caption:"Entries",
        onSelectRow: function(id){
            if(id && id!==lastSel){ 
               $('#entries').restoreRow(lastSel); 
               lastSel=id; 
            }
          $('#entries').editRow(id, true); 
        },
    });
    
    $("#entries").jqGrid('navGrid','#pager',{edit:false,add:true,del:false});

    $(function() {
        $( "input:submit, a, button", ".page" ).button();
    });
    
    
    
});