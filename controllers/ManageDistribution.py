#!/usr/bin/env python
# coding: utf-8
import web
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
        render_dict = commonDistribution.assign(post_data)  
        project_list = [] 
        info_dict = {}   
        query_set = []    
        if post_data.get('item_id', '')=='110':   ##仅针对添加内容页面
            project_list = model_to_object(get_project_list())        
        if 'show_pid' in post_data:            
            query_set = get_project_info(post_data['show_pid'])
        if 'show_itemid' in post_data:            
            query_set = get_item_text(post_data['show_itemid'])    
        object = model_to_object(query_set)
        if object:
            info_dict = object[0]
        info_dict['project_list'] = project_list    
        render_dict['item_content'] = template_to_html(render_dict['item_content'], info_dict)
        return render_dict
    
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
    if 'project_name' in post_data:        ##项目更新
        project_name = post_data.get('project_name', '')
        project_descrip = post_data.get('project_descrip', '')

        if not project_name.strip():
            errorCode = -1
            message = "项目名不能为空"
        else: 
            if not post_data.get('pid', ''):   ##没有pid，即新内容
                pid = insert_project(project_name, project_descrip, "")
            else:
                pid = post_data.get('pid')
            header_html = '<div align="right"><a href="/docmaster?pid=%s">进入项目</a> | <a href="/docmaster/manage?item_id=109&show_pid=%s">编辑</a> | <a href="#commit">评论</a> |<a href="#commit"> 纠错</a></div>' % (pid,pid)            
            if update_project(pid, project_name, project_descrip, header_html + mark_content(project_descrip)):
                html = "更新项目成功！"
            else:
                errorCode = -3
                message = "更新项目失败,不能重命名！"
    elif 'item_name' in post_data:     ##内容更新
        pid = post_data.get('project_list', '0')
        item_name = post_data.get('item_name', '')
        item_content = post_data.get('item_content', '')
        item_order = post_data.get('item_order', '-1')
        if not item_order.isdigit():
            item_order = -1
        if pid=='0':
            errorCode = -1
            message = "项目名不能为空！"      
        else:
            if not post_data.get('item_id', ''):   ##无数据
                itemid = insert_item(pid, item_name, item_order, item_content, '')
            else:
                itemid = post_data.get('item_id', '')
            header_html = '<div align="right"><a href="/docmaster/manage?item_id=110&show_itemid=%s">编辑</a> | <a href="#commit">评论</a> |<a href="#commit"> 纠错</a></div>' % itemid                                 
            if update_item(itemid, pid, item_name, item_order, item_content, header_html + mark_content(item_content)):
                html = "更内容成功！"
            else:
                errorCode = -3
                message = "更新内容失败!"             
    else:
        errorCode = -3
        message = "传递的参数不正确！"
    return {
            'html' : html, 
            'errorCode' : errorCode, 
            'message' : message
    }
    
    