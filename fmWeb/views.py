# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

class DisableCSRFCheck(object):
    """
    屏蔽csrf验证
    """
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)