#!/usr/bin/env python
# coding: utf-8

def bind_data(user_dict, page_name):
    data_dict = { 'user_dict' : user_dict }
    data_dict[page_name + '_active'] = "active"
    return data_dict

def model_to_object(model):
    t_list = []
    if model:        
        for line in model:
            t_list.append(dict(line))
    return t_list

def object_to_json(*object):
    import json
    return json.dumps(object)

def mark_content(content):
    import markdown
    import markdowncode
    configs = {}
    myext = markdowncode.CodeExtension(configs=configs)  ##自定义插件
    return markdown.markdown(content, extensions=[myext])

def template_to_html(template, *pars):
    import web
    template = web.template.Template(template)
    return template(*pars)

def islogin(user_dict):
    if not user_dict.get('id'):
        return False
    else:
        return True
    
def user_auth(post_data, user_dict):
    email = post_data.get('email', '')
    passwd = post_data.get('passwd', '')
    if email=='five3@163.com' and passwd=='111111':
        user_dict['email'] = email
        user_dict['id'] = 100
        user_dict['name'] = email.split("@")[0]
        user_dict['privilege'] = 0
        return True
    else:
        return False

def makesitemaptxt(makeids):   
    turls = ['http://seleniumhq.testdoc.org\n']
    try:
        for line in makeids:
            turls.append('http://testdoc.org/docmaster?pid=%s&item_id=%s\n' % (line.pid, line.id))     
        f = open('./static/docServer/sitemap.txt', 'w')
        f.writelines(turls)
        return True
    except(e):
        return False
