#!/usr/bin/env python
# coding: utf-8
from config.settings import db
from Item import now

def log(ip, method, path, data, agent):
    insert_sql = '''insert into trace (ip, method, path, data, agent, time) Values ($ip, $method, $path, $data, $agent, now())'''
    return db.query(insert_sql, vars=locals())
#     return db.insert('trace', ip=ip, method=method, path=path, data=data, agent=agent, time='now()')

