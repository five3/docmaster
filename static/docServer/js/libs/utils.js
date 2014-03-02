function init(){
	$('img').click(function(){
		var imgurl = $(this).attr('src');
		window.open(imgurl);
	});
}