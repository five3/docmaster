#!/usr/bin/env python
# coding: utf-8

pre_fix = 'views.'
pre_url = '/docmaster'
##URL匹配可以使用正则
urls = (
    pre_url + '/?',                        pre_fix + 'DocMaster.Home',
    pre_url + '/manage',                        pre_fix + 'DocMaster.Manage',
    pre_url + '/search',                        pre_fix + 'DocMaster.Search',
    pre_url + '/login',                        pre_fix + 'DocMaster.Login',
)
