#!/usr/bin/env python
# coding: utf-8
from config.settings import db
from Item import now

def login_record(ip):
    return db.insert('login', ip=ip, time=now())

def login_fail(name, times):
    if times < 2:
        return db.insert('loginfail', times=times, name=name)
    else:
        return db.update('loginfail', times=times, where='name=$name', vars=locals())

def get_fail_times(name):
    r = db.select('loginfail', what='times', where='name=$name', vars=locals())
    if r:       
        return r[0].times
    else:
        return 0