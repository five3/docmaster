#!/usr/bin/env python
# coding: utf-8
from config.settings import db
from Item import now

def insert_project(project_name, project_descrip, html):
    pid = db.insert('project', name=project_name, create_date=now())
    print pid
    if pid:
        itemid = db.insert('item', pid=99, title=project_name, 
                          text=project_descrip, html=html, create_date=now()) 
    if pid and itemid:
        return pid
    else:
        return False

def get_project_info(pid):
    return db.query('select p.id, p.name, i.text from project p, item i \
    where p.id=$pid and i.pid=99 and p.name=i.title', vars=locals())
    
def get_project_list():
    return db.select('project', what='id, name', where='id>=100')

def update_project(pid, project_name, project_descrip, html):
    query_str = r'''update item i, project p 
                  set i.title='%s', i.text='%s', i.html='%s', i.update_date='%s' 
                  where p.id=%s and p.name=i.title and i.pid=99''' % (project_name.replace("'", "\\'"), 
                                                                      project_descrip.replace("'", "\\'"), 
                                                                      html.replace("'", "\\'"), 
                                                                      now(), pid)
#    print query_str
    item_rlt = db.query(query_str)
    project_rlt = db.update('project', name=project_name, update_date=now(), where='id=%s' % pid)
    if item_rlt and project_rlt:
        return True
    else:
        return False
