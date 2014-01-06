#!/usr/bin/env python
# coding: utf-8

def bind_data(user_dict, page_name):
    data_dict = { 'user_dict' : user_dict }
    data_dict[page_name + '_active'] = "active"
    return data_dict

def model_to_object(model):
    t_list = []
    if model:        
        for line in model:
            t_list.append(dict(line))
    return t_list

def object_to_json(*object):
    import json
    return json.dumps(object)

def mark_content(content):
    import markdown
    return markdown.markdown(content)

    