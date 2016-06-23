# -*- coding: utf-8 -*-
import serializers as sl
import filter as fl
import models as md
from rest_framework import viewsets
from django.db.models import Q

class TbAreaViewSet(viewsets.ModelViewSet):

    queryset = md.TbArea.objects.all()
    serializer_class = sl.TbAreaSerializer
    filter_class = fl.TbAreaFilter


class TbCropsinfoViewSet(viewsets.ModelViewSet):

    queryset = md.TbCropsinfo.objects.all()
    serializer_class = sl.TbCropsinfoSerializer
    filter_class = fl.TbCropsinfoFilter


class TbFertilizerinfoViewSet(viewsets.ModelViewSet):

    queryset = md.TbFertilizerinfo.objects.all()
    serializer_class = sl.TbFertilizerinfoSerializer
    filter_class = fl.TbFertilizerinfoFilter


class TbFieldViewSet(viewsets.ModelViewSet):

    queryset = md.TbField.objects.all()
    serializer_class = sl.TbFieldSerializer
    filter_class = fl.TbFieldFilter


class TbPesticidesinfoViewSet(viewsets.ModelViewSet):

    queryset = md.TbPesticidesinfo.objects.all()
    serializer_class = sl.TbPesticidesinfoSerializer
    filter_class = fl.TbPesticidesinfoFilter


class TbPutfertilizerViewSet(viewsets.ModelViewSet):

    queryset = md.TbPutfertilizer.objects.all()
    serializer_class = sl.TbPutfertilizerSerializer
    filter_class = fl.TbPutfertilizerFilter


class TbPutpesticidesViewSet(viewsets.ModelViewSet):

    queryset = md.TbPutpesticides.objects.all()
    serializer_class = sl.TbPutpesticidesSerializer
    filter_class = fl.TbPutpesticidesFilter


class TbRealtimedataViewSet(viewsets.ModelViewSet):

    # queryset = md.TbRealtimedata.objects.all()
    serializer_class = sl.TbRealtimedataSerializer
    filter_class = fl.TbRealtimedataFilter

    def get_queryset(self):
        try:
            if self.request._request.GET:
                if self.request._request.GET['warning'] == "history":
                    return md.TbRealtimedata.objects.filter(Q(readstatus=1) | Q(readstatus=2)).order_by('-collecttime')
                elif self.request._request.GET['warning'] == "realtime":
                    return md.TbRealtimedata.objects.filter(readstatus=1).order_by('-collecttime')
                else:
                    md.TbRealtimedata.objects.all().order_by('-collecttime')
        except:
            return md.TbRealtimedata.objects.all().order_by('-collecttime')
        return md.TbRealtimedata.objects.all().order_by('-collecttime')



class TbTreatmanageViewSet(viewsets.ModelViewSet):

    queryset = md.TbTreatmanage.objects.all()
    serializer_class = sl.TbTreatmanageSerializer
    filter_class = fl.TbTreatmanageFilter


class TbWarnlimitViewSet(viewsets.ModelViewSet):

    queryset = md.TbWarnlimit.objects.all()
    serializer_class = sl.TbWarnlimitSerializer
    filter_class = fl.TbWarnlimitFilter