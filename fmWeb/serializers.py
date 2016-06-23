# -*- coding: utf-8 -*-
import models as md
from rest_framework import serializers
from django.db import transaction


class TbAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.TbArea
        fields = (
            'areaid', 'areacode', 'areaname'
        )


class TbCropsinfoSerializer(serializers.ModelSerializer):

    cropspic = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)
    class Meta:
        model = md.TbCropsinfo
        fields = (
            'cropsinfoid', 'cropsname', 'cropsdesc', 'cropslife', 'cropspic'
        )


class TbFertilizerinfoSerializer(serializers.ModelSerializer):

    fertilizerpic = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)
    class Meta:
        model = md.TbFertilizerinfo
        fields = (
            'fertilizerinfoid', 'fertilizername', 'fertilizerdesc', 'usedesc', 'fertilizerpic'
        )

class TbFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.TbField
        fields = (
            'fieldid', 'fieldcode', 'fieldname', 'fkey_areaid'
        )


class TbPesticidesinfoSerializer(serializers.ModelSerializer):

    pesticidespic = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False)
    class Meta:
        model = md.TbPesticidesinfo
        fields = (
            'pesticidesinfoid', 'pesticidesname', 'pesticidesdesc', 'usedesc', 'pesticidespic'
        )



class TbPutfertilizerSerializer(serializers.ModelSerializer):

    usetime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = md.TbPutfertilizer
        fields = (
            'putfertilizerid', 'fkey_areaid', 'fkey_fieldid', 'usetime', 'fkey_fertilizerinfoid', 'consum'
        )



class TbPutpesticidesSerializer(serializers.ModelSerializer):

    usetime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')

    class Meta:
        model = md.TbPutpesticides
        fields = (
            'putpesticidesid', 'fkey_areaid', 'fkey_fieldid', 'usetime', 'fkey_pesticidesinfoid', 'consum'
        )



class TbRealtimedataSerializer(serializers.ModelSerializer):

    collecttime = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    readstatus = serializers.IntegerField(allow_null=True)

    class Meta:
        model = md.TbRealtimedata
        fields = (
            'reartimeid', 'fkey_areaid', 'fkey_fieldid', 'collecttime', 'readstatus', 'temperdata', 'humiditydata', 'phdata'
        )

    def create(self, validated_data):
        limit = md.TbWarnlimit.objects.all()
        limitmintem = limit[0].min_temperlimit
        limitmaxtem = limit[0].max_temperlimit
        limitminhum = limit[0].min_water
        limitmaxhum = limit[0].max_water
        limitminph = limit[0].min_ph
        limitmaxph = limit[0].max_ph
        with transaction.atomic():
            if validated_data['temperdata'] < limitmintem or validated_data['temperdata'] > limitmaxtem or validated_data['humiditydata'] < limitminhum or validated_data['humiditydata'] > limitmaxhum or validated_data['phdata'] < limitminph or validated_data['phdata'] > limitmaxph:
                validated_data['readstatus'] = 1
            else:
                validated_data['readstatus'] = 0
            realtimedatarecords = md.TbRealtimedata.objects.create(**validated_data)
            return realtimedatarecords


class TbTreatmanageSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.TbTreatmanage
        fields = (
            'cropstreatmanageid', 'fkey_cropsinfoid', 'crops_treattime', 'suggestreaptime', 'yield_field', 'status'
        )



class TbWarnlimitSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.TbWarnlimit
        fields = (
            'warmlimitid', 'min_temperlimit', 'max_temperlimit', 'max_ph', 'min_ph', 'min_water', 'max_water'
        )
