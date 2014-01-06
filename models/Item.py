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
    item_list = db.select('item', what='id, title', where='pid=$pid', order="item_order", vars=locals())
    return item_list


def get_item_content(itemid):
    item_content = db.select('item', what='html', where='id=$itemid', vars=locals())
    return item_content

def insert_item(pid, item_name, item_order, item_content, html):
    itemid = db.insert('item', pid=pid, title=item_name, item_order=item_order, 
                       text=item_content, html=html, create_date=now()) 
    if itemid:
        return True
    else:
        return False
    