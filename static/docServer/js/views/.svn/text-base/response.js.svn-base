function showPerview(rep){
	var json = eval(rep)[0];
	if (json.errorCode != 0){
		alert(json.message);
	}else{
		$('#perviewDiv').html(json.html);
	}
}

function showSubmit(rep){
	var json = eval(rep)[0];
	if (json.errorCode != 0){
		alert(json.message);
	}else{
		alert(json.html);
		refresh();
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