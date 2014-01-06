#!/usr/bin/env python
# coding: utf-8
from libs.utils import *
from models.Base import query as querydb

def assign(post_data): 
    if post_data.get('type', '') == 'db':
        query_set = search_in_db(post_data)
        if query_set:
            return {
                'data' : model_to_object(query_set), 
                'errorCode' : 0, 
                'message' : ''                   
                }            
        else:
            return {
                'html' : '', 
                'errorCode' : -2, 
                'message' : '没有搜索到内容！'                   
                }
    else:
        return {
            'html' : '', 
            'errorCode' : -1, 
            'message' : '传输的参数类型错误！'
            }
    
def search_in_db(post_data):
    table_name = post_data.get('table_name', '')
    what = post_data.get('what', '')
    where = post_data.get('where', '')
    query = post_data.get('query', '')
    if not query.strip():
        query = 'select %s from %s where %s' % [what, table_name, where]
    query_set = querydb(query)
    return query_set
    