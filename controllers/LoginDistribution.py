#!/usr/bin/env python
# coding: utf-8
from libs.utils import *
from models.Login import *
import web
def assign(post_data):
    import time     
    email = post_data.get('email', '')
    t = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    name = email+t
    times = get_fail_times(name)
    if times<3 and user_auth(post_data, web.config._session.user):         
        ip = web.ctx.env.get('REMOTE_ADDR')                  
        login_record(ip)
        return web.seeother("/docmaster/manage")
    else:            
        login_fail(name, times+1)
        return web.seeother("/docmaster/login")
    


    