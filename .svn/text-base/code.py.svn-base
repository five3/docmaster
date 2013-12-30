#!/usr/bin/env python  
#encoding: utf-8
from config.url import urls
import web
import os
#web.config.debug = False
web.config.session_parameters['timeout'] = 86400 #24 * 60 * 60, # 24 hours   in seconds
web.config.session_parameters['ignore_expiry'] = False
web.config['static_dir'] = os.getenv("RESOURCE_SERVER_ROOT", "../resourceServer/static")
web.config['work_dir'] = os.getcwd()

app = web.application(urls, locals())
#if web.config.get("_session") is None:
#    from web import utils
#    store = web.session.DiskStore('sessions')
#    user = utils.Storage({
#                          "id": "",
#                          "name": "",
#                          "email": "",
#                          "privilege": "",
#                          })
#    session = web.session.Session(app, store, 
#                                  initializer={
#                                               "status": 0,
#                                               "user": user,
#                                               })
#    web.config._session = session
#else:
#    session = web.config._session

import sys
print sys.getdefaultencoding()
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()

if __name__ == "__main__":
    app.run()

