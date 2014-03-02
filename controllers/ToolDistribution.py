#!/usr/bin/env python
# coding: utf-8
from models.Item import *
from libs.utils import *
import web

def assign(post_data):
    errorcode = -1
    message = '无成功操作'
    type = post_data.get('type', '')
    if type == 'sitemaptxt':
        makeids = get_pids_with_itemid()         
        if makesitemaptxt(makeids):
            errorcode = 0
            message = '生成sitemap文件成功!'
        else:
            errorcode = 1000
            message = '生成sitemap文件失败！'
    return {
            'errorcode' : errorcode, 
            'message' : message,
            }   