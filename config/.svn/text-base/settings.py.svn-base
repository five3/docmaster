#!/usr/bin/env python
# coding: utf-8
import web
import os

db = web.database(dbn='mysql', db='doc_master', user='root', pw='password', charset='utf8', host="10.255.254.129")
render = web.template.render('templates/', cache=False)

web.config.debug = True

config = web.storage(
    admin_email='chenxiaowu@dangdang.com',
    site_name = 'docMaster',
    site_desc = 'help doc publish on web',
    site_auther = 'XiaowuChen',    
    resources = '/static',
)
web.config['site_info'] = config
##设置为模板文件中的全局变量
web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
web.template.Template.globals['db'] = db
#web.template.Template.globals['session'] = web.config._session

