# _*_ coding:utf-8 _*_
__author__ = 'wuqy'
__date__ = '2021/8/9 14:35'

from django import forms


class LoginFrom(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=4)
