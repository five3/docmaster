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
    return db.select('item', what='id, title', where='pid=$pid', order="item_order", vars=locals())
     
def get_item_content(itemid):
    return db.select('item', what='title, html', where='id=$itemid', vars=locals())

def get_item_text(itemid):
    return db.select('item', what='id, pid, item_order, title, text', where='id=$itemid', vars=locals())

def insert_item(pid, item_name, item_order, item_content, html):
    return db.insert('item', pid=pid, title=item_name, item_order=item_order, 
                       text=item_content, html=html, create_date=now()) 
    
def update_item(item_id, pid, item_name, item_order, item_content, html):
    return db.update('item', where='id=%s'%item_id, pid=pid, title=item_name, text=item_content, 
              html=html, item_order=item_order, update_date=now())