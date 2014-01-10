function showPerview(rep){
	var json = eval(rep)[0];
	if (json.errorCode != 0){
		alert(json.message);
	}else{
		$('#perviewDiv').html(json.html);
		SyntaxHighlighter.config.clipboardSwf = "/static/common/js/libs/syntaxhighlighter/clipboard.swf";
		SyntaxHighlighter.all();
		$('body').load();
	}
}

function showSubmit(rep){
	var json = eval(rep)[0];
	if (json.errorCode != 0){
		alert(json.message);
	}else{
		alert(json.html);
//		refresh();
	}
}

function showProjectList(rep){
	var json = eval(rep)[0];
	if (json.errorCode != 0){
		alert(json.message);
	}else{
		updateSelect('project_list', json.data);
	}	
}