#!/usr/bin/env python
# coding: utf-8
import web
pre_fix = 'views.'
pre_url = '/docmaster'
##URL匹配可以使用正则
urls = (
    '/',                                   pre_fix + 'DocMaster.Index',
    '/sitemap(\.txt)',                         pre_fix + 'DocMaster.sitemap',
    pre_url + '/?',                        pre_fix + 'DocMaster.Home',
    pre_url + '/manage',                        pre_fix + 'DocMaster.Manage',
    pre_url + '/search',                        pre_fix + 'DocMaster.Search',
    pre_url + '/login',                        pre_fix + 'DocMaster.Login',
    pre_url + '/tool',                        pre_fix + 'DocMaster.Tool',
)
