$(document).ready(function(){
    //Construct a jqGrid object
    $(".entries").jqGrid({
       	url:'/_get_entries',
    	datatype: "json",
       	colNames:['id','name', 'type', 'library','from_buss','to_buss', 'length', 'ampacity'],
       	colModel:[
       		{name:'id',index:'id', width:55},
       		{name:'name',index:'name', width:90},
       		{name:'type',index:'type', width:80, align:"right"},
       		{name:'library',index:'library', width:80, align:"right"},		
       		{name:'from_buss',index:'from_buss', width:80,align:"right"},		
       		{name:'to_buss',index:'to_buss', width:80, sortable:false},
       		{name:'length',index:'length', width:80,align:"right"},		
       		{name:'ampacity',index:'ampacity', width:80, sortable:false}
       	],
       	rowNum:10,
       	rowList:[10,20,30],
       	pager: '#pager',
       	sortname: 'id',
        viewrecords: true,
        sortorder: "desc",
        caption:"Entries"
    });
    $(".entries").jqGrid('navGrid','#pager',{edit:false,add:false,del:false});

    $(function() {
        $( "input:submit, a, button", ".page" ).button();
    });
    
    
    
});