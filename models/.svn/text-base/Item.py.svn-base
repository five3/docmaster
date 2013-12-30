#!/usr/bin/env python
# coding: utf-8
from config.settings import db

def now():
    '''
    @获取当前时间戳
    '''
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def get_item_list(pid):
    item_list = db.select('item', what='id, title', where='pid=$pid', vars=locals())
    return item_list


def get_item_content(itemid):
    item_content = db.select('item', what='html', where='id=$itemid', vars=locals())
    return item_content