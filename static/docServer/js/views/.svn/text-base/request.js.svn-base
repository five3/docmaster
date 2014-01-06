function previewAction(contentId){
	var perviewContent = $('#'+contentId).val();
	if (perviewContent == ''){ alert('预览内容不能为空！'); return;}
	var data = {
			'type': 'preview',
			'content': perviewContent,			
	}
	ajaxPost('/docmaster/manage', data, showPerview);
}

function submitAction(formId, actionUrl, event){
	var data = getFormData(formId);	
	data += 'type=submit';	
	ajaxPost(actionUrl, data, event);
}

function addProject(){
	var pname = $('#project_name').val();
	if ($.trim(pname)==''){ alert('项目名不能为空！'); return ;}
	var pds = $('#project_descrip').val();
	if ($.trim(pds)==''){ alert('项目描述不能为空！'); return ;}
	submitAction('project_form', '/docmaster/manage', showSubmit);
}

function addItem(){
	var pid = $('#project_list').val();
	if (pid=='0'){ alert('项目名不能为空！'); return ;}
	var title = $('#item_name').val();
	if ($.trim(title)==''){ alert('子项标题不能为空！'); return ;}
	var content = $('#item_content').val();
	if ($.trim(content)==''){ alert('子项描述不能为空！'); return ;}
	submitAction('item_form', '/docmaster/manage', showSubmit);
}