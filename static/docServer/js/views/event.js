function view_project(){
	var pid = $('#project_list').val();
	if (pid == 0){
		alert('你当前没有选择项目！');
	}else{
		var url = "/docmaster?pid=" + pid;
		window.open(url);
	}
}