# -*- coding: utf-8 -*-
import models as md
import rest_framework_filters as filters

# filter

class TbAreaFilter(filters.FilterSet):

    areacode = filters.AllLookupsFilter(name="areacode", lookup_type='contains')
    areaname = filters.AllLookupsFilter(name="areaname", lookup_type='contains')

    class Meta:
        model = md.TbArea


class TbCropsinfoFilter(filters.FilterSet):

    cropsname = filters.AllLookupsFilter(name="cropsname", lookup_type='contains')
    cropsdesc = filters.AllLookupsFilter(name="cropsdesc", lookup_type='contains')
    cropslife = filters.AllLookupsFilter(name="cropslife", lookup_type='contains')

    class Meta:
        model = md.TbCropsinfo


class TbFertilizerinfoFilter(filters.FilterSet):

    fertilizername = filters.AllLookupsFilter(name="fertilizername", lookup_type='contains')
    fertilizerdesc = filters.AllLookupsFilter(name="fertilizerdesc", lookup_type='contains')
    usedesc = filters.AllLookupsFilter(name="usedesc", lookup_type='contains')

    class Meta:
        model = md.TbFertilizerinfo


class TbFieldFilter(filters.FilterSet):

    fieldcode = filters.AllLookupsFilter(name="fieldcode", lookup_type='contains')
    fieldname = filters.AllLookupsFilter(name="fieldname", lookup_type='contains')
    fkey_areaid = filters.RelatedFilter(TbAreaFilter, name="fkey_areaid")

    class Meta:
        model = md.TbField


class TbPesticidesinfoFilter(filters.FilterSet):

    pesticidesname = filters.AllLookupsFilter(name="pesticidesname", lookup_type='contains')
    pesticidesdesc = filters.AllLookupsFilter(name="pesticidesdesc", lookup_type='contains')
    usedesc = filters.AllLookupsFilter(name="usedesc", lookup_type='contains')

    class Meta:
        model = md.TbPesticidesinfo


class TbPutfertilizerFilter(filters.FilterSet):

    fkey_areaid = filters.RelatedFilter(TbAreaFilter, name="fkey_areaid")
    fkey_fieldid = filters.RelatedFilter(TbFieldFilter, name="fkey_fieldid")
    usetime = filters.AllLookupsFilter(name="usetime", lookup_type='contains')
    fkey_fertilizerinfoid = filters.RelatedFilter(TbFertilizerinfoFilter, name="fkey_fertilizerinfoid")
    consum = filters.AllLookupsFilter(name="consum", lookup_type='contains')

    class Meta:
        model = md.TbPutfertilizer


class TbPutpesticidesFilter(filters.FilterSet):

    fkey_areaid = filters.RelatedFilter(TbAreaFilter, name="fkey_areaid")
    fkey_fieldid = filters.RelatedFilter(TbFieldFilter, name="fkey_fieldid")
    usetime = filters.AllLookupsFilter(name="usetime", lookup_type='contains')
    fkey_pesticidesinfoid = filters.RelatedFilter(TbPesticidesinfoFilter, name="fkey_pesticidesinfoid")
    consum = filters.AllLookupsFilter(name="consum", lookup_type='contains')

    class Meta:
            model = md.TbPutpesticides


class TbRealtimedataFilter(filters.FilterSet):

    fkey_areaid = filters.RelatedFilter(TbAreaFilter, name="fkey_areaid")
    fkey_fieldid = filters.RelatedFilter(TbFieldFilter, name="fkey_fieldid")
    collecttime = filters.AllLookupsFilter(name="collecttime", lookup_type='contains')
    readstatus = filters.AllLookupsFilter(name="readstatus", lookup_type='exact')
    temperdata = filters.AllLookupsFilter(name="temperdata", lookup_type='contains')
    humiditydata = filters.AllLookupsFilter(name="humiditydata", lookup_type='contains')
    phdata = filters.AllLookupsFilter(name="phdata", lookup_type='contains')

    class Meta:
        model = md.TbRealtimedata


class TbTreatmanageFilter(filters.FilterSet):

    fkey_cropsinfoid = filters.RelatedFilter(TbCropsinfoFilter, name="fkey_cropsinfoid")
    crops_treattime = filters.AllLookupsFilter(name="crops_treattime", lookup_type='contains')
    suggestreaptime = filters.AllLookupsFilter(name="suggestreaptime", lookup_type='contains')
    yield_field = filters.AllLookupsFilter(name="yield_field", lookup_type='contains')
    status = filters.AllLookupsFilter(name="status", lookup_type='contains')

    class Meta:
        model = md.TbTreatmanage



class TbWarnlimitFilter(filters.FilterSet):

    min_temperlimit = filters.AllLookupsFilter(name="min_temperlimit", lookup_type='contains')
    max_temperlimit = filters.AllLookupsFilter(name="max_temperlimit", lookup_type='contains')
    max_ph = filters.AllLookupsFilter(name="max_ph", lookup_type='contains')
    min_ph = filters.AllLookupsFilter(name="min_ph", lookup_type='contains')
    min_water = filters.AllLookupsFilter(name="min_water", lookup_type='contains')
    max_water = filters.AllLookupsFilter(name="max_water", lookup_type='contains')

    class Meta:
        model = md.TbWarnlimit
