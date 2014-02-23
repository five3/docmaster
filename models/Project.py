#!/usr/bin/env python
# coding: utf-8
from config.settings import db
from Item import now

def insert_project(project_name, project_descrip, html):
    pid = db.insert('project', name=project_name, description=project_descrip, create_date=now())
    if pid:
        return pid
    else:
        return False

def get_project_info(pid):
    return db.query('select p.id, p.name, i.despcription from project p where p.id=$pid', vars=locals())
    
def get_project_list():
    return db.select('project', what='id, name', where='id>=99')

def update_project(pid, project_name, project_descrip, html):
    project_rlt = db.update('project', name=project_name, description=project_descrip, update_date=now(), where='id=%s' % pid)
    if project_rlt:
        return True
    else:
        return False
