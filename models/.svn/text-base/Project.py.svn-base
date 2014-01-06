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
        return True
    else:
        return False

