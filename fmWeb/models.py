from __future__ import unicode_literals

from django.db import models

# Create your models here.

def get_cropspic(instance, filename):
    return 'templates/pictures/cropspic/'+filename

def get_fertilizerpic(instance, filename):
    return 'templates/pictures/fertilizerpic/'+filename

def get_pesticidespic(instance, filename):
    return 'templates/pictures/pesticidespic/'+filename



class TbArea(models.Model):
    areaid = models.AutoField(primary_key=True)
    areacode = models.CharField(max_length=20, blank=True, null=True)
    areaname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_area'
        ordering = ['areaid']

    def __unicode__(self):
        return '%d:%s' % (self.areaid, self.areaname)


class TbCropsinfo(models.Model):
    cropsinfoid = models.AutoField(primary_key=True)
    cropsname = models.CharField(max_length=20, blank=True, null=True)
    cropsdesc = models.CharField(max_length=300, blank=True, null=True)
    cropslife = models.BigIntegerField(blank=True, null=True)
    cropspic = models.ImageField(upload_to=get_cropspic, blank=True, null=True)
    # cropspic = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_cropsinfo'
        ordering = ['cropsinfoid']

    def __unicode__(self):
        return '%d:%s' % (self.cropsinfoid, self.cropsname)



class TbFertilizerinfo(models.Model):
    fertilizerinfoid = models.AutoField(primary_key=True)
    fertilizername = models.CharField(max_length=20, blank=True, null=True)
    fertilizerdesc = models.CharField(max_length=300, blank=True, null=True)
    usedesc = models.CharField(max_length=300, blank=True, null=True)
    fertilizerpic = models.ImageField(upload_to=get_fertilizerpic, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_fertilizerinfo'
        ordering = ['fertilizerinfoid']

    def __unicode__(self):
        return '%d:%s' % (self.fertilizerinfoid, self.fertilizername)


class TbField(models.Model):
    fieldid = models.AutoField(primary_key=True)
    fieldcode = models.BigIntegerField(blank=True, null=True)
    fieldname = models.CharField(max_length=50, blank=True, null=True)
    fkey_areaid = models.ForeignKey(TbArea, related_name='field', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_areaid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_field'
        ordering = ['fieldid']

    def __unicode__(self):
        return '%d:%s' % (self.fieldid, self.fieldname)



class TbPesticidesinfo(models.Model):
    pesticidesinfoid = models.AutoField(primary_key=True)
    pesticidesname = models.CharField(max_length=20, blank=True, null=True)
    pesticidesdesc = models.CharField(max_length=200, blank=True, null=True)
    usedesc = models.CharField(max_length=200, blank=True, null=True)
    pesticidespic = models.ImageField(upload_to=get_pesticidespic, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_pesticidesinfo'
        ordering = ['pesticidesinfoid']



class TbPutfertilizer(models.Model):
    putfertilizerid = models.AutoField(primary_key=True)
    fkey_areaid = models.ForeignKey(TbArea, related_name='putfertilizer', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_areaid = models.BigIntegerField(blank=True, null=True)
    fkey_fieldid = models.ForeignKey(TbField, related_name='putfertilizer', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_fieldid = models.BigIntegerField(blank=True, null=True)
    usetime = models.DateTimeField(blank=True, null=True)
    fkey_fertilizerinfoid = models.ForeignKey(TbFertilizerinfo, related_name='putfertilizer', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_fertilizercode = models.BigIntegerField(blank=True, null=True)
    consum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_putfertilizer'
        ordering = ['putfertilizerid']



class TbPutpesticides(models.Model):
    putpesticidesid = models.AutoField(primary_key=True)
    fkey_areaid = models.ForeignKey(TbArea, related_name='putpesticides', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_areaid = models.BigIntegerField(blank=True, null=True)
    fkey_fieldid = models.ForeignKey(TbField, related_name='putpesticides', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_fieldid = models.BigIntegerField(blank=True, null=True)
    usetime = models.DateTimeField(blank=True, null=True)
    fkey_pesticidesinfoid = models.ForeignKey(TbPesticidesinfo, related_name='putpesticides', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_pesticidescode = models.BigIntegerField(blank=True, null=True)
    consum = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_putpesticides'
        ordering = ['putpesticidesid']



class TbRealtimedata(models.Model):
    reartimeid = models.AutoField(primary_key=True)
    fkey_areaid = models.ForeignKey(TbArea, related_name='realtimedata', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_areanameid = models.BigIntegerField(blank=True, null=True)
    fkey_fieldid = models.ForeignKey(TbField, related_name='realtimedata', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_fieldnameid = models.BigIntegerField(blank=True, null=True)
    collecttime = models.DateTimeField(blank=True, null=True)
    readstatus = models.IntegerField(blank=True, null=True)
    temperdata = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    humiditydata = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    phdata = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_realtimedata'
        ordering = ['-collecttime']



class TbTreatmanage(models.Model):
    cropstreatmanageid = models.AutoField(primary_key=True)
    fkey_cropsinfoid = models.ForeignKey(TbCropsinfo, related_name='treatmanage', blank=True, null=True, on_delete=models.SET_NULL)
    # fkey_cropsinfo = models.BigIntegerField(blank=True, null=True)
    crops_treattime = models.TimeField(blank=True, null=True)
    suggestreaptime = models.TimeField(blank=True, null=True)
    yield_field = models.DecimalField(db_column='yield', max_digits=8, decimal_places=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    status = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_treatmanage'
        ordering = ['cropstreatmanageid']



class TbWarnlimit(models.Model):
    warmlimitid = models.AutoField(primary_key=True)
    min_temperlimit = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
    max_temperlimit = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
    max_ph = models.BigIntegerField(blank=True, null=True)
    min_ph = models.BigIntegerField(blank=True, null=True)
    min_water = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
    max_water = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_warnlimit'
        ordering = ['warmlimitid']
