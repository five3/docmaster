#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from libs.utils import *
from controllers import HomeDistribution, ManageDistribution, SearchDistribution

render = settings.render
db = settings.db

class Home:
    def GET(self):
#        user_dict = web.config._session.user
        user_dict = {}
        render_content = HomeDistribution.assign(web.input())
        data_dict = bind_data(user_dict, 'home')
        data_dict['render_content'] = render_content
        return render.home(data_dict)
    
    def POST(self):        
        return object_to_json(HomeDistribution.assign(web.input()))
           
class Manage:
    def GET(self):
#        user_dict = web.config._session.user
        user_dict = {}
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
    