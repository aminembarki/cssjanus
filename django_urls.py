#!/usr/bin/python
#
# Copyright 2008 Google Inc. All Rights Reserved.

__author__ = 'elsigh@google.com (Lindsey Simon)'

from django.conf.urls.defaults import *

urlpatterns = patterns('',
  (r'^$', 'django_cssjanus.index'),
  (r'^do/', 'django_cssjanus.do'),
  (r'^\/?files/(?P<path>.*)$', 'django.views.static.serve', 
    {'document_root': '/home/elsigh/public_html/cssjanus'}),
)