#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

proj_path = os.path.dirname(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fm_web.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import fmWeb.models as md
import threading
import random
from django.db import transaction

def yellow(str):
    YELLOW = '\033[1;33m'
    ENDC = '\033[0m'
    return YELLOW + str + ENDC


def main():

    timeSleeper = threading.Timer(5, main)
    timeSleeper.start()

    datalist = [{'key': "1", 'value': '水稻'}, {'key': "2", 'value': '小麦'}, {'key': "3", 'value': '玉米'}]
    data = random.choice(datalist)

    with transaction.atomic():
        print yellow('编号：'+data['key']+'    '+'名称：'+data['value'])
        tbarea = md.TbArea(areacode=data['key'], areaname=data['value'])
        tbarea.save()

if __name__ == "__main__":
    main()