#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from libs.utils import *
from controllers import HomeDistribution, ManageDistribution, SearchDistribution,LoginDistribution, ToolDistribution

render = settings.render
db = settings.db

class Index:
    def GET(self):
        return web.seeother('/docmaster')
    
class Home:
    def GET(self):
        logip()
        user_dict = web.config._session.user
        render_content = HomeDistribution.assign(web.input())
        data_dict = bind_data(user_dict, 'home')
        data_dict['render_content'] = render_content
        return render.home(data_dict)
    
    def POST(self):  
        logip()      
        return object_to_json(HomeDistribution.assign(web.input()))
           
class Manage:
    def GET(self):
        logip()
        user_dict = web.config._session.user
        if not islogin(user_dict):
            return web.seeother('/docmaster/login')        
        render_content = ManageDistribution.assign(web.input())
        data_dict = bind_data(user_dict, 'manage')
        data_dict['render_content'] = render_content
        return render.manage(data_dict)
    
    def POST(self):  
        logip()      
        return object_to_json(ManageDistribution.assign(web.input()))
        
class Search:
    def GET(self):
        self.POST();
    
    def POST(self):
        logip()
        return object_to_json(SearchDistribution.assign(web.input()))

class Login:
    def GET(self):
        logip()
        return render.login()
    
    def POST(self):
        logip()
        post_data = web.input()                      
        return LoginDistribution.assign(post_data)
        
class Tool:
    def GET(self):
        logip()
        post_data = web.input()
        return object_to_json(ToolDistribution.assign(post_data))
    def POST(self):
        return this.Get()       
    
class sitemap:
    def GET(self, ext):
        logip()
        if ext.strip()=='.txt':
            web.seeother('/static/docServer/sitemap.txt')
        if ext.strip()=='.xml':    
            web.seeother('/static/docServer/sitemap.xml')
            