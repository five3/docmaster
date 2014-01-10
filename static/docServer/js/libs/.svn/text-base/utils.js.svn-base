function init(){
	$$("#leftside .list-group a").click(
			function(){										
				$$(this).parent().children("a").removeClass("active");
				$$(this).addClass("active");
				$$.ajax({ 
					url: "/docmaster/", 
					async: true,
					type: "POST",
					data: {
						"type": "item",
						"itemid": $$(this).attr('itemid')
					},
					contentType: "application/x-www-form-urlencoded",		
					context: this, 		
					cache: false,
					success: function(data){
						var json = eval(data)
    					$$("#rightbody").html(json[0].item_content); 
    					SyntaxHighlighter.all();    	       								
  					},
					complete: function(data){
    					SyntaxHighlighter.all();    	       								
  					},
				});      					
	});
}