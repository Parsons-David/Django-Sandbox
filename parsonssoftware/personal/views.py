# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'personal/index.html')

def about(request):
    return render(request, 'personal/about.html')

def projects(request):
    return render(request, 'personal/projects.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content' : ['If you would like to contact me, please email me.', 'david.parsons@rutgers.edu']})
