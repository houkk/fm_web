"""fm_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from fmWeb import tests
from fmWeb import restful as rf
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tbarea', rf.TbAreaViewSet)
router.register(r'tbcropsinfo', rf.TbCropsinfoViewSet)
router.register(r'tbfertilizerinfo', rf.TbFertilizerinfoViewSet)
router.register(r'tbfield', rf.TbFieldViewSet)
router.register(r'tbpesticidesinfo', rf.TbPesticidesinfoViewSet)
router.register(r'tbputfertilizer', rf.TbPutfertilizerViewSet)
router.register(r'tbputpesticides', rf.TbPutpesticidesViewSet)
router.register(r'tbrealtimedata', rf.TbRealtimedataViewSet, base_name="realtimedata")
router.register(r'tbtreatmanage', rf.TbTreatmanageViewSet)
router.register(r'tbwarnlimit', rf.TbWarnlimitViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^test/$', tests.test),
    url(r'^$', tests.test),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
