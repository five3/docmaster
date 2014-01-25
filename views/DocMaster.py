#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from libs.utils import *
from controllers import HomeDistribution, ManageDistribution, SearchDistribution,LoginDistribution

render = settings.render
db = settings.db

class Home:
    def GET(self):
        user_dict = web.config._session.user
        render_content = HomeDistribution.assign(web.input())
        data_dict = bind_data(user_dict, 'home')
        data_dict['render_content'] = render_content
        return render.home(data_dict)
    
    def POST(self):        
        return object_to_json(HomeDistribution.assign(web.input()))
           
class Manage:
    def GET(self):
        user_dict = web.config._session.user
        if not islogin(user_dict):
            return render.login()        
        render_content = ManageDistribution.assign(web.input())
        data_dict = bind_data(user_dict, 'manage')
        data_dict['render_content'] = render_content
        return render.manage(data_dict)
    
    def POST(self):        
        return object_to_json(ManageDistribution.assign(web.input()))
        
class Search:
    def GET(self):
        self.POST();
    
    def POST(self):
        return object_to_json(SearchDistribution.assign(web.input()))

class Login:
    def GET(self):
        return render.login()
    
    def POST(self):
        post_data = web.input()
        if auth(post_data, web.config._session.user):
            return web.seeother("/docmaster/manage")
        else:
            return web.seeother("/docmaster/login")
            
    