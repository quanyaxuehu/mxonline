# _*_ coding:utf-8 _*_
__author__ = 'wuqy'
__date__ = '2021/7/19 17:05'

import xadmin

from .models import UserAsk,CourseComments,UserMessage,UserCourse,UserFavorite


class UserAskAdmin(object):
    list_display = ['name', 'mobile','course_name','add_time']
    search_fields = ['name', 'mobile','course_name']
    list_filter = ['name', 'mobile','course_name','add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course','comments','add_time']
    search_fields =['user', 'course','comments']
    list_filter =['user__nick_name', 'course__name','comments','add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id','fav_type','add_time']
    search_fields = ['user', 'fav_id','fav_type']
    list_filter = ['user__nick_name', 'fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message','has_read','add_time']
    search_fields = ['user', 'message','has_read']
    list_filter = ['user', 'message','has_read','add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course','add_time']
    search_fields =['user', 'course']
    list_filter =['user__nick_name', 'course__name','add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
