#!/usr/bin/env python
# coding: utf-8
import commonDistribution
from libs.utils import *
from models.Item import *
from models.Project import *

def assign(post_data): 
    if post_data.get('type', '') == 'preview':
        return preview_action(post_data)
    elif post_data.get('type', '') == 'submit':
        return submit_action(post_data)
    else:
        post_data['pid'] = '98'  
        return commonDistribution.assign(post_data)
    
def preview_action(post_data):
    html = ''
    errorCode = 0
    message = ''    
    content = post_data.get('content', '')
    if content.strip():
        html = mark_content(content)
    else:
        errorCode = -1
        message = "预览内容不能为空！"
    return {
            'html' : html, 
            'errorCode' : errorCode, 
            'message' : message
    }
    
def submit_action(post_data):
    html = ''
    errorCode = 0
    message = ''
    if 'project_name' in post_data:        
        project_name = post_data.get('project_name', '')
        project_descrip = post_data.get('project_descrip', '')
        if not project_name.strip():
            errorCode = -1
            message = "项目名不能为空"
        elif insert_project(project_name, project_descrip, mark_content(project_descrip)):
            html = "添加项目成功！"
        else:
            errorCode = -2
            message = "添加项目失败,不能重命名！"
    elif 'item_name' in post_data:
        pid = post_data.get('project_list', '0')
        item_name = post_data.get('item_name', '')
        item_content = post_data.get('item_content', '')
        item_order = post_data.get('item_order', '-1')
        if not item_order.isdigit():
            item_order = -1
        if pid=='0':
            errorCode = -1
            message = "项目ID不能为0！"            
        elif insert_item(pid, item_name, item_order, item_content, mark_content(item_content)):
            html = '添加内容成功！'
        else:
            errorCode = -2
            message = "添加内容失败！"            
    else:
        errorCode = -3
        message = "传递的参数不正确！"
    return {
            'html' : html, 
            'errorCode' : errorCode, 
            'message' : message
    }
    
    