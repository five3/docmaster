#!/usr/bin/env python
# coding: utf-8
from models.Item import *
from libs.utils import *

def assign(post_data):
    type = post_data.get('type', 'project')
    if type == 'project':        
        pid = post_data.get('pid', '99')
        item_list = model_to_object(get_item_list(pid))
        if item_list:
            item_content = get_item_content(item_list[0].get('id'))
        else:
            item_content = ''            
        if item_content:
            item_content = item_content[0].get('html', '')
        return {
                'item_list' : model_to_object(item_list), 
                'item_content' : item_content
                }            
    elif type == 'item':
        itemid = post_data.get('itemid', '0')
        item_content = get_item_content(itemid)
        if item_content:
            item_content = item_content[0].get('html', '')
        else:
            item_content = ''
        return {
                'item_content' : item_content
                }
    else:
        return {}
    