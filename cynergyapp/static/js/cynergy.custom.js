$(document).ready(function(){
    
    //Construct a jqGrid object
    $("#entries").jqGrid({
       	url:'/_get_entries',
    	datatype: "json",
       	colNames:['name', 'type', 'library','from_buss','to_buss', 'length', 'ampacity'],
       	colModel:[
       		{name:'name',index:'name', width:90},
       		{name:'type',index:'type', width:80, align:"right"},
       		{name:'library',index:'library', width:80, align:"center"},		
       		{name:'from_buss',index:'from_buss', width:80,align:"center"},		
       		{name:'to_buss',index:'to_buss', width:80, sortable:false, align:"center"},
       		{name:'length',index:'length', width:80,align:"center"},		
       		{name:'ampacity',index:'ampacity', width:80, sortable:false,align:"center"}
       	],
       	rowNum:10,
       	rowList:[10,20,30],
       	pager: '#pager',
       	sortname: 'id',
        viewrecords: true,
        width: '905',
        sortorder: "desc",
        caption:"Entries",
        onSelectRow: function(id) {
          $('#entries').editRow(id, true); 
        },
    });
    
    $("#entries").jqGrid('navGrid','#pager',{edit:false,add:false,del:false});

    $(function() {
        $( "input:submit, a, button", ".page" ).button();
    });
    
    
    
});