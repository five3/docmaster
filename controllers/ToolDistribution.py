#!/usr/bin/env python
# coding: utf-8
from models.Item import *
from libs.utils import *
import web

def assign(post_data):
    errorcode = -1
    message = '无成功操作'
    type = post_data.get('type', '')
    if type == 'makerobot':
        makeids = get_pids_with_itemid()         
        if makerobot(makeids):
            errorcode = 0
            message = '生成搜索引擎文件成功!'
        else:
            errorcode = 1000
            message = '生成搜索引擎文件失败！'
    return {
            'errorcode' : errorcode, 
            'message' : message,
            }   