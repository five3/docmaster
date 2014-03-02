#!/usr/bin/env python
# coding: utf-8
from config.settings import db

def now():
    '''
    @获取当前时间戳
    '''
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def get_item_list(pid, is_visible=1):
    '''左侧显示列表'''
    return db.select('item', what='id, title', where='pid=$pid and is_visible=$is_visible', order="item_order", vars=locals())
     
def get_item_content(itemid):
    '''右侧显示文章区'''
    return db.select('item', what='title, html', where='id=$itemid', vars=locals())

def get_item_text(itemid):
    '''编辑页面，更新信息回显'''
    return db.select('item', what='id, pid, item_order, is_visible, title, text', where='id=$itemid', vars=locals())

def insert_item(pid, item_name, item_order, item_content, html, is_visible):
    return db.insert('item', pid=pid, title=item_name, item_order=item_order, 
                       text=item_content, html=html, is_visible=is_visible, create_date=now()) 
    
def update_item(item_id, pid, item_name, item_order, item_content, html, is_visible):
    return db.update('item', where='id=%s'%item_id, pid=pid, title=item_name, text=item_content, 
              html=html, item_order=item_order, is_visible=is_visible, update_date=now())
    
def get_pids_with_itemid():
    return db.select('item', what='id, pid', where='pid>=99')