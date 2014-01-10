#!/usr/bin/env python
# coding: utf-8
from models.Item import *
from libs.utils import *

def assign(post_data):
    type = post_data.get('type', 'project')
    if type == 'project':        
        item_id = '0'        
        item_content = {}
        pid = post_data.get('pid', '99')
        item_list = model_to_object(get_item_list(pid))
        if item_list:
            item_id = post_data.get('item_id', item_list[0].get('id'))
            item_content = get_item_content(item_id)    
        if item_content:
            item_content = item_content[0]
        else:
            item_content = {}
        return {
                'item_list' : model_to_object(item_list), 
                'item_id' : item_id,
                'item_content' : item_content.get('html', ''),
                'title' : item_content.get('title', ''),
                'pid' : pid,
                }            
#    elif type == 'item':
#        itemid = post_data.get('itemid', '0')
#        item_content = get_item_content(itemid)
#        if item_content:
#            item_content = item_content[0]
#        else:
#            item_content = {}
#        return {
#                'item_content' : item_content.get('html', ''), 
#                'item_id' : itemid, 
#                'title' : item_content.get('title', '')
#                }
    else:
        return {}
    